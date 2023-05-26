import pandas as pd
import graph
import requests
from bs4 import BeautifulSoup

def get_oscars_data() -> list[dict[str, str]]:
    url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', {'class': 'wikitable sortable'})
    if table is None or isinstance(table, str):
        return []
    rows = table.find_all('tr')

    data: list[dict[str, str]] = []
    i = 0
    for row in rows[1:]:
        cols = row.find_all('td')
        title = cols[0].text.strip()
        year = cols[1].text.strip()
        awards = cols[2].text.strip()
        nominations = cols[3].text.strip()
        link = cols[0].find('a').get('href')
        if title=="Flesh and Sand (Carne y arena)" or int(awards) < 1:
            continue
        data.append({'title': title, 'year': year, 'awards': awards, 'nominations': nominations, 'link': link})
        i += 1
        if i == 30:
            print(f'Ano final {year}')
            break

    return data

import json
import os


def memoize_movie_data(func):
    def wrapper(movie_link):
        title = movie_link.split('/')[-1]
        file_name = f"cache/{title}.json"
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                return json.load(f)
        else:
            result = func(movie_link)
            with open(file_name, "w") as f:
                json.dump(result, f)
            return result
    return wrapper


@memoize_movie_data
def get_movie_data(movie_link) -> dict[str, str]:
    url = f'https://en.wikipedia.org{movie_link}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox vevent'})
    if infobox is None or isinstance(infobox, str):
        return {}
    rows = infobox.find_all('tr')

    data: dict[str, str] = {}
    for row in rows:
        header = row.find('th')
        if header and header.text == 'Directed by':
            director = row.find('td').text.strip()
            data['director'] = director
        if header and header.text == 'Starring':
            actors = row.find('td').text.strip().split('\n')
            data['actors'] = actors

    return data

def get_movies_data() -> list[dict[str, str]]:
    oscars_data = get_oscars_data()

    movies_data = []
    for i, movie in enumerate(oscars_data):
        title = movie['title']
        movie_id = i + 1
        movie_data = get_movie_data(movie['link'])
        director = movie_data.get('director', 'N/A')
        actors = movie_data.get('actors', [])
        
        if director == 'N/A':
            continue
        
        movies_data.append({'id': movie_id, 'title': title, 'director': director, 'actors': actors})

    return movies_data

def get_actors_graph(movies_data):
    g = graph.Graph()

    actors = set()
    for movie in movies_data:
        for actor in movie['actors']:
            actors.add(actor)
            g.add_node(graph.Node(actor))
        if len(actors) > 50:
            break
        
    for movie in movies_data:
        for actor in movie['actors']:
            for other_actor in movie['actors']:
                if actor != other_actor and actor in actors and other_actor in actors:
                    g.add_edge(actor, other_actor)

    return g

def memoize_graph(func):
    def wrapper():
        file_name = "cache/actors_graph"
        if os.path.exists(file_name + '_edges.csv'):
            return graph.Graph().load(file_name)
                
        else:
            result = func()
            result.save(file_name)
            return result
    return wrapper


def graph_from_actors() -> graph.Graph:
    movies_data = get_movies_data()
    g = get_actors_graph(movies_data)
    return g