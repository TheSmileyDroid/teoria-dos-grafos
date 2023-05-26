import graph as g
from make_gif import make_gif

def is_isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False
    if len(graph1[0]) != len(graph2[0]):
        return False
    edges_g1: list[int] = list(map(sum, graph1))
    edges_g2: list[int] = list(map(sum, graph2))
    sorted_edges_g1 = sorted(edges_g1)
    sorted_edges_g2 = sorted(edges_g2)
    if sorted_edges_g1 == sorted_edges_g2:
        return True
    return False

def remove_node(graph, node) -> list[list[int]]:
    new_graph = []
    edges = []
    for i in range(len(graph[0])):
        if graph[node][i] == 1:
            edges.append(i)
    for i in range(len(graph)):
        if i == node:
            continue
        new_node = []
        for j in range(len(graph[i])):
            if j not in edges:
                new_node.append(graph[i][j])
            else:
                new_node.append(0)
        new_graph.append(new_node)
    return new_graph

def remove_edge(graph, edge) -> list[list[int]]:
    new_graph = []
    for i in range(len(graph)):
        new_node = []
        for j in range(len(graph[i])):
            if j == edge:
                continue
            new_node.append(graph[i][j])
        new_graph.append(new_node)
    return new_graph

def is_subgraph(graph, subgraph) -> bool:
    if is_isomorphic(graph, subgraph):
        return True
    if len(graph) < len(subgraph):
        return False
    if len(graph[0]) < len(subgraph[0]):
        return False
    for i in range(len(graph)):
        new_graph = remove_node(graph, i)
        if is_subgraph(new_graph, subgraph):
            return True
        for j in range(len(graph[i])):
            new_graph = remove_edge(graph, j)
            if is_subgraph(new_graph, subgraph):
                return True
    return False

i_r = 0

def is_subgraph_export(graph, subgraph) -> bool:
    global i_r
    if is_isomorphic(graph, subgraph):
        return True
    if len(graph) < len(subgraph):
        return False
    if len(graph[0]) < len(subgraph[0]):
        return False
    i_r=i_r+1
    g1 = g.Graph().convert_from_incidence_matrix(graph)

    g1.write_png(f'.tests/graph1_{i_r:02}.png', splines='false')
    for i in range(len(graph)):
        new_graph = remove_node(graph, i)
        if is_subgraph_export(new_graph, subgraph):
            return True
        for j in range(len(graph[i])):
            new_graph = remove_edge(graph, j)
            if is_subgraph_export(new_graph, subgraph):
                return True
    return False


g1_ = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
]

g2_ = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

g1v = g.Graph().convert_from_incidence_matrix(g1_)
g2v = g.Graph().convert_from_incidence_matrix(g2_)

print(g1v)
print(g2v)

g1v.write_png(f'.tests/graph1_00.png', splines='false')
g1v.write_png(f'graph1_00.png', splines='false')
g2v.write_png(f'graph2_00.png', splines='false')


print(is_subgraph_export(g1_,g2_))
make_gif('.tests', 'animation.gif')