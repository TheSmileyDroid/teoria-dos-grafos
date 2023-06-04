from src.types.graph import Graph


def shortest_path(graph: Graph, start: str, end: str) -> list[str]:
    if start not in graph.get_vertices():
        raise ValueError(f"Start vertex '{start}' not found in graph")
    if end not in graph.get_vertices():
        raise ValueError(f"End vertex '{end}' not found in graph")

    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if vertex == end:
            return path

        if vertex not in visited:
            for adjacent in graph.get_neighbours(vertex):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

            visited.add(vertex)

    return []
