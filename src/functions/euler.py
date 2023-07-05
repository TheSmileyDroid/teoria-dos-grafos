from src.structs.graph import Graph


def is_euler_graph(graph: Graph) -> bool:
    if not graph.is_connected():
        return False

    # Verifica se todos os vértices possuem grau par
    for vertex in graph.get_vertices():
        if len(graph.get_neighbors(vertex)) % 2 != 0:
            return False

    return True
