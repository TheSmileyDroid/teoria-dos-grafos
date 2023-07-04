from typing import Generator
from src.functions.paths import shortest_path
from src.importer.text_importer import load_graph_from_set
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


def is_spanning_tree(graph: Graph, spanning_tree: Graph) -> bool:
    if not is_tree(spanning_tree):
        return False

    if spanning_tree.get_num_vertices() != graph.get_num_vertices():
        return False

    if spanning_tree.get_num_edges() != graph.get_num_vertices() - 1:
        return False

    if not spanning_tree.is_connected():
        return False

    return True


def calculate_distance_between_trees(A1: Graph, A2: Graph) -> int:
    direct_sum = set(A1.get_edges()) ^ set(A2.get_edges())

    return len(direct_sum) // 2


def find_first_spanning_tree(graph: Graph) -> Graph:
    closed = set()
    edges: list[tuple[str, str]] = []

    q = [list(graph.get_vertices())[0]]
    closed.add(q[0])

    while len(q) > 0:
        v = q.pop(0)
        for neighbor in graph.get_neighbors(v):
            if neighbor not in closed:
                closed.add(neighbor)
                edges.append((v, neighbor))
                q.append(neighbor)

    return load_graph_from_set(graph.get_vertices(), set(edges))


def find_spanning_trees_using_chords(tree: Graph, chords: list[tuple[str, str]]) -> Generator[Graph, None, None]:
    for chord in chords:
        circuit = shortest_path(tree, chord[0], chord[1])
        # print('circuit: ', circuit)
        for i in range(len(circuit) - 1):
            edge_to_remove = (circuit[i], circuit[i + 1])
            # print('edge to remove: ', edge_to_remove)
            edges = tree.get_edges().copy()
            if (edge_to_remove[0], edge_to_remove[1]) in edges:
                edges.remove((edge_to_remove[0], edge_to_remove[1]))
            else:
                edges.remove((edge_to_remove[1], edge_to_remove[0]))
            edges.add(chord)
            yield load_graph_from_set(set(), edges)

            new_chords = chords.copy()
            new_chords.remove(chord)
            yield from find_spanning_trees_using_chords(load_graph_from_set(set(), edges), new_chords)


def find_spanning_tree(graph: Graph) -> Generator[Graph, None, None]:
    tree0 = find_first_spanning_tree(graph)

    # print('tree1: ', tree1.get_edges())
    yield tree0

    # print('graph: ', graph.get_edges())
    # print('tree1: ', tree1.get_edges())

    chords: list[tuple[str, str]] = []
    for edge in graph.get_edges():
        if set(edge) not in map(set, tree0.get_edges()):
            chords.append(edge)

    # print('chords: ', chords)

    yield from find_spanning_trees_using_chords(tree0, chords)


def find_n_spanning_trees(graph: Graph, n: int) -> Generator[Graph, None, None]:
    trees = find_spanning_tree(graph)
    for i in range(n):
        yield next(trees)


def find_all_spanning_trees(graph: Graph) -> list[Graph]:
    trees = find_spanning_tree(graph)
    return list(trees)


def maxi_distance(tree: Graph, all_spanning_tree: list[Graph]) -> int:
    maxi = 0
    for spanning_tree in all_spanning_tree:
        distance = calculate_distance_between_trees(tree, spanning_tree)
        if distance > maxi:
            maxi = distance
    return maxi


def central_tree(graph: Graph) -> Graph:
    trees = find_all_spanning_trees(graph)
    center = find_first_spanning_tree(graph)
    maxi = maxi_distance(center, trees)

    for tree in trees:
        distance = maxi_distance(tree, trees)
        if distance < maxi:
            maxi = distance
            center = tree

    return center
