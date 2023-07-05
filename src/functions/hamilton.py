from src.structs.graph import Graph


def has_hamiltonian_cycle(graph: Graph):
    visited = set()

    def dfs(vertex: str, start: str):
        visited.add(vertex)
        if len(visited) == len(graph.get_vertices()):
            if start in graph.get_neighbors(vertex):
                return True
        else:
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    if dfs(neighbor, start):
                        return True
        visited.remove(vertex)
        return False

    for vertex in graph.get_vertices():
        visited.clear()
        if dfs(vertex, vertex):
            return True

    return False
