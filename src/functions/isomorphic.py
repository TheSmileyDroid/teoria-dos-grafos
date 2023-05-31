from src.types.graph import Graph


def is_isomorphic(graph1: Graph, graph2: Graph):
    if graph1.is_directed() != graph2.is_directed():
        return False

    if graph1.get_num_vertices() != graph2.get_num_vertices():
        return False

    if graph1.get_num_edges() != graph2.get_num_edges():
        return False

    # Check if the degree sequence of the vertices match
    degree_sequence1 = sorted(
        [len(graph1.get_adjacent_vertices(v)) for v in graph1.get_vertices()]
    )
    degree_sequence2 = sorted(
        [len(graph2.get_adjacent_vertices(v)) for v in graph2.get_vertices()]
    )
    if degree_sequence1 != degree_sequence2:
        return False

    return True
