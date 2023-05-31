from src.types.graph import Graph


def is_subgraph(graph1: Graph, graph2: Graph) -> bool:
    if graph2.is_directed() != graph1.is_directed():
        return False

    if graph2.get_num_vertices() > graph1.get_num_vertices():
        return False

    if graph2.get_num_edges() > graph1.get_num_edges():
        return False

    for vertex in graph2.get_vertices():
        if vertex not in graph1.get_vertices():
            return False

    for edge in graph2.get_edges():
        if edge not in graph1.get_edges():
            return False

    return True


def is_graph_vertex_disjoint(graph1: Graph, graph2: Graph) -> bool:
    for vertex in graph1.get_vertices():
        if vertex in graph2.get_vertices():
            return False

    return True


def is_graph_edge_disjoint(graph1: Graph, graph2: Graph) -> bool:
    for edge in graph1.get_edges():
        if edge in graph2.get_edges():
            return False

    return True
