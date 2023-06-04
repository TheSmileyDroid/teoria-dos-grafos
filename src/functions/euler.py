from src.types.graph import Graph


def is_euler_graph(graph: Graph) -> bool:
    if not graph.is_connected():
        return False

    # Check if all vertices have even degree
    for vertex in graph.get_vertices():
        if len(graph.get_neighbours(vertex)) % 2 != 0:
            return False

    return True
