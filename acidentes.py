from src.exporter.dot import export_to_pydot
import pandas as pd
from src.structs.graph import Graph
import progressbar  # type: ignore

# "id";"data_inversa";"dia_semana";"horario";"uf";"br";"km";"municipio";"causa_acidente";"tipo_acidente";"classificacao_acidente";"fase_dia";"sentido_via";"condicao_metereologica";"tipo_pista";"tracado_via";"uso_solo";"pessoas";"mortos";"feridos_leves";"feridos_graves";"ilesos";"ignorados";"feridos";"veiculos";"latitude";"longitude";"regional";"delegacia";"uop"
data = pd.read_csv('datatran2022.csv',
                   delimiter=';', encoding='iso-8859-1')

# Convert , to . in km column
data['km'] = data['km'].str.replace(',', '.')
# Keep only SP data
data = data[data['uf'] == 'SP']
# Remove Vera Cruz, Marilia
data = data[data['municipio'] != 'VERA CRUZ']
data = data[data['municipio'] != 'MARILIA']
data = data[data['municipio'] != 'SAO JOSE DO RIO PRETO']
data = data[data['municipio'] != 'ICEM']
data = data[data['municipio'] != 'ONDA VERDE']
data = data[data['municipio'] != 'NOVA GRANADA']
data = data[data['municipio'] != 'BADY BASSITT']
data = data[data['municipio'] != 'JACI']
data = data[data['municipio'] != 'MIRASSOL']
data = data[data['municipio'] != 'JOSE BONIFACIO']
data = data[data['municipio'] != 'UBARANA']
data = data[data['municipio'] != 'PROMISSAO']
data = data[data['municipio'] != 'GUAICARA']
data = data[data['municipio'] != 'LINS']
data = data[data['municipio'] != 'GETULINA']
data = data[data['municipio'] != 'GUAIMBE']
data = data[data['municipio'] != 'OCAUCU']
data = data[data['municipio'] != 'CAMPOS NOVOS PAULISTA']
data = data[data['municipio'] != 'RIBEIRAO DO SUL']
data = data[data['municipio'] != 'SAO PEDRO DO TURVO']
data = data[data['municipio'] != 'OURINHOS']
data = data[data['municipio'] != 'SALTO GRANDE']

g1: Graph = Graph()


def memoize(f):
    memory = {}

    def inner(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]

    return inner


@memoize
def mean_of_km_of_municipio_in_br(br: float, municipio: str):
    data_br = data[data['br'] == br]
    data_municipio_br = data_br[data_br['municipio'] == municipio]

    return data_municipio_br['km'].astype(float, errors='ignore').mean()


bar = progressbar.ProgressBar(maxval=len(data.index), widgets=[
    progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

bar.start()

for i, row in data.iterrows():
    bar.update(
        bar.currval + 1 if bar.currval + 1 < len(data.index) else len(data.index))
    for municipio1 in data['municipio'].unique():
        for municipio2 in data['municipio'].unique():
            if municipio1 != municipio2:
                mean1 = mean_of_km_of_municipio_in_br(
                    row['br'], municipio1)
                mean2 = mean_of_km_of_municipio_in_br(
                    row['br'], municipio2)
                if abs(mean1 - mean2) > 70:
                    continue
                if mean1 > mean2:
                    if float(row['km']) < mean1 and float(row['km']) > mean2:
                        g1.add_edge((municipio1, municipio2))
                        g1.add_edge_weight(
                            (municipio1, municipio2),
                            g1.get_edge_weight((municipio1, municipio2)) + 1
                        )
                else:
                    if float(row['km']) > mean1 and float(row['km']) < mean2:
                        g1.add_edge((municipio2, municipio1))
                        g1.add_edge_weight(
                            (municipio2, municipio1),
                            g1.get_edge_weight((municipio2, municipio1)) + 1
                        )

bar.finish()

print(g1.get_edge_weights())
export_to_pydot(g1).write_png('acidentes.png')  # type: ignore
