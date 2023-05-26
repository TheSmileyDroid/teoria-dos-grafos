import pydot
import graph

def new_graph(
    splines='true', 
    overlap='false', 
    concentrate='true', 
    nodesep='0.1', 
    layout='sfdp', 
    beautify='false',
    ):
    g = pydot.Dot(
        graph_type='graph', 
        rankdir='LR', 
        splines=splines,
        overlap=overlap,
        concentrate=concentrate,
        nodesep=nodesep,
        layout=layout,
        beautify=beautify,
    )
    
    g.set_node_defaults(
        shape='circle',
        style='filled',
        fontsize='12',
        fontname='fira sans',
        width='1',
        height='1',
        fixedsize='true',
        fillcolor='#8dd3c7ff',
        layer='top',
    )
    
    g.set_edge_defaults(
        arrowsize='0.5',
        fontsize='8',
        fontname='fira sans',
        color='#08306bff',
        penwidth='2.0',
    )
    
    return g

def edgelist_to_adjacency_matrix(edgelist: list[tuple[str, str]]) -> list[list[int]]:
    nodes = set()
    for edge in edgelist:
        nodes.add(edge[0])
        nodes.add(edge[1])
    nodes = list(nodes)
    nodes.sort()
    
    matrix = []
    for i in range(len(nodes)):
        row = []
        for j in range(len(nodes)):
            row.append(0)
        matrix.append(row)
    
    for edge in edgelist:
        i = nodes.index(edge[0])
        j = nodes.index(edge[1])
        matrix[i][j] = 1
        matrix[j][i] = 1
    
    return matrix
        
def adjacency_matrix_to_edgelist(matrix: list[list[int]]) -> list[tuple[str, str]]:
    edgelist = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 1:
                edgelist.append((i, j))
    return edgelist

def edgelist_to_incidence_matrix(edgelist: list[tuple[str, str]]) -> list[list[int]]:
    nodes = set()
    for edge in edgelist:
        nodes.add(edge[0])
        nodes.add(edge[1])
    nodes = list(nodes)
    nodes.sort()
    
    matrix = []
    for i in range(len(nodes)):
        row = []
        for j in range(len(edgelist)):
            row.append(0)
        matrix.append(row)
    
    for i in range(len(edgelist)):
        edge = edgelist[i]
        j = nodes.index(edge[0])
        matrix[j][i] = 1
        j = nodes.index(edge[1])
        matrix[j][i] = 1
    
    return matrix

def incidence_matrix_to_edgelist(matrix: list[list[int]]) -> list[tuple[str, str]]:
    edgelist = []
    for i in range(len(matrix[0])):
        edge = []
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                edge.append(j)
        edgelist.append(tuple(edge))
    return edgelist

def adjacency_matrix_to_adjacency_list(matrix: list[list[int]]) -> dict[str, list[str]]:
    adjacency_list = {}
    for i in range(len(matrix)):
        adjacency_list[i] = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list

def adjacency_list_to_adjacency_matrix(adjacency_list: dict[str, list[str]]) -> list[list[int]]:
     g = graph.Graph().convert_from_adjacency_list(adjacency_list)
     return g.convert_to_adjacency_matrix()

def adjacency_list_to_incidence_matrix(adjacency_list: dict[str, list[str]]) -> dict[dict[int]]:
    g = graph.Graph().convert_from_adjacency_list(adjacency_list)
    return g.convert_to_incidence_matrix()

def incidence_matrix_to_adjacency_list(matrix: list[list[int]]) -> dict[str, list[str]]:
    g = graph.Graph().convert_from_incidence_matrix(matrix)
    return g.convert_to_adjacency_list()

def adjacency_matrix_to_incidence_matrix(matrix: list[list[int]]) -> list[list[int]]:
    g = graph.Graph().convert_from_adjacency_matrix(matrix)
    return g.convert_to_incidence_matrix()