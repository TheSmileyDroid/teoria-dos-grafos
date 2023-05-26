from src.types.graph import Graph


def shortest_path(graph: Graph, start: str, end: str) -> list[str]:
    """
    Finds the shortest path between two vertices in a graph.

    :param graph: The graph to search through.
    :param start: The starting vertex.
    :param end: The ending vertex.
    :return: A list of vertices in the shortest path.
    """

    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex == end:
            return path

        if vertex not in visited:
            for adjacent in graph.get_vertex(vertex).get_adjacent():
                new_path = list(path)
                new_path.append(adjacent.get_name())
                queue.append(new_path)

            visited.add(vertex)

    return []
