import os
import graph
import csv
import progressbar as pb
import graph

def memoize_graph(func):
    def wrapper():
        file_name = "cache/acidente_graph"
        if os.path.exists(file_name + '_edges.csv'):
            return graph.Graph().load(file_name)
                
        else:
            result = func()
            result.save(file_name)
            return result
    return wrapper

@memoize_graph
def graph_from_acidente() -> graph.Graph:
    g = graph.Graph()

    with open('filtered/datatran2018_SP.csv', 'r', encoding = 'unicode_escape') as f:
        # id, data_inversa, dia_semana, horario, uf, br, km, municipio, causa_acidente, tipo_acidente, classificacao_acidente, fase_dia, sentido_via, condicao_metereologica, tipo_pista, tracado_via, uso_solo, pessoas, mortos, feridos_leves, feridos_graves, ilesos, ignorados, veiculos
        reader = csv.reader(f, delimiter=';')

        brs = []

        rows = list(reader)

        progress_1 = pb.ProgressBar(maxval=len(rows)).start()

        done = set()

        for row in rows:
                brs.append({'br': row[5], 'km': row[6], 'municipio': row[7]})
                if row[7] in done:
                    continue
                g.add_node(graph.Node(row[7]))
                done.add(row[7])
                progress_1.update(progress_1.currval + 1)
        
        progress_1.finish()

        progress_2 = pb.ProgressBar(maxval=len(brs)).start()

        for br in set([b['br'] for b in brs]):
            cities = set([b['municipio'] for b in brs if b['br'] == br])
            if len(cities) > 1:
                for city in cities:
                    for other_city in cities:
                        if city != other_city:
                            if [b['km'].replace(',','.') for b in brs if b['br'] == br and b['municipio'] == city][0] == 'NA':
                                continue
                            distance = abs(float([b['km'].replace(',','.') for b in brs if b['br'] == br and b['municipio'] == city][0]) - float([b['km'].replace(',','.') for b in brs if b['br'] == br and b['municipio'] == other_city][0]))
                            if distance < 70:
                                edge = g.get_edge(city, other_city)
                                if not edge:
                                    g.add_edge(city, other_city, label=br, weight=1)
                                else:
                                    edge.weight += 1
            progress_2.update(progress_2.currval + 1)

        progress_2.finish()

        
    return g