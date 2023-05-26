import os
import pandas as pd
import graph
import urllib.request
import progressbar

pbar = None

def memoize_graph(func):
    def wrapper():
        file_name = "cache/rotas_graph"
        if os.path.exists(file_name + '_edges.csv'):
            return graph.Graph().load(file_name)
        else:
            result = func()
            result.save(file_name)
            return result
    return wrapper

@memoize_graph
def graph_from_rotas() -> graph.Graph:
    os.makedirs('cache', exist_ok=True)
    if not os.path.exists('raw/Dados_Estatisticos.csv'):
        print('Baixando dados da ANAC...')
        
        def show_progress(block_num, block_size, total_size):
            global pbar
            if pbar is None:
                pbar = progressbar.ProgressBar(maxval=total_size)
                pbar.start()

            downloaded = block_num * block_size
            if downloaded < total_size:
                pbar.update(downloaded)
            else:
                pbar.finish()
                pbar = None

        urllib.request.urlretrieve('https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20opera%C3%A7%C3%B5es%20a%C3%A9reas/Dados%20Estat%C3%ADsticos%20do%20Transporte%20A%C3%A9reo/Dados_Estatisticos.csv', 'raw/Dados_Estatisticos.csv', show_progress)

    df = pd.read_csv('raw/Dados_Estatisticos.csv', skiprows=1, sep=';') # type: ignore
    brasil_rows = df[(df['AEROPORTO_DE_ORIGEM_PAIS'] == 'BRASIL') & (df['AEROPORTO_DE_DESTINO_PAIS'] == 'BRASIL')]
    brasil_rows = brasil_rows[(brasil_rows['EMPRESA_SIGLA'] == 'LAN')]

    g = graph.Graph()

    print('Criando nós...')

    for index, row in brasil_rows.iterrows():
        if row['DISTANCIA_VOADA_KM'] == '':
            continue
        if row['AEROPORTO_DE_ORIGEM_NOME'] not in g.nodes:
            g.add_node(graph.Node(row['AEROPORTO_DE_ORIGEM_NOME']))
        if row['AEROPORTO_DE_DESTINO_NOME'] not in g.nodes:
            g.add_node(graph.Node(row['AEROPORTO_DE_DESTINO_NOME']))
        g.add_edge(row['AEROPORTO_DE_ORIGEM_NOME'], row['AEROPORTO_DE_DESTINO_NOME'], row['DISTANCIA_VOADA_KM'])
        
    return g
