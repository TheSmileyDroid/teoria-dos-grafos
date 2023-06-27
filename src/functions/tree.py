from src.types.graph import Graph
from src.types.abc_graph import GraphABC
from queue import Queue


def is_tree(graph: GraphABC) -> bool:
    if not graph.is_connected():
        return False

    n = graph.get_num_vertices()
    m = graph.get_num_edges()
    if m != n - 1:
        return False

    return True


def distance_between_vertices(graph: Graph, v1: str, v2: str) -> int:
    q: Queue = Queue()
    visited = set()

    q.put((v1, 0))
    visited.add(v1)

    while not q.empty():
        vertex, distance = q.get()

        if vertex == v2:
            return distance

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                q.put((neighbor, distance + 1))
                visited.add(neighbor)

    return -1


def distance_of_other_vertices(graph: Graph, v1: str) -> dict[str, int]:
    q: Queue = Queue()
    visited = set()

    q.put((v1, 0))
    visited.add(v1)

    distances = dict[str, int]()
    while not q.empty():
        vertex, distance = q.get()

        distances[vertex] = distance

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                q.put((neighbor, distance + 1))
                visited.add(neighbor)

    return distances


def eccentricity(graph: Graph, v1: str) -> int:
    distances = distance_of_other_vertices(graph, v1)
    return max(distances.values())


def tree_center(graph: Graph) -> list[str]:
    if not is_tree(graph):
        raise ValueError("Graph is not a tree.")
    center = []

    min_eccentricity = float('inf')

    for vertex in graph.get_vertices():
        eccentricity = max(distance_of_other_vertices(graph, vertex).values())

        if eccentricity < min_eccentricity:
            center = [vertex]
            min_eccentricity = eccentricity
        elif eccentricity == min_eccentricity:
            center.append(vertex)

    return center
