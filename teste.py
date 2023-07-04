from src.functions.paths import shortest_path
from src.types.graph import Graph
from src.importer.text_importer import load_graph_from_set
from typing import Generator
from src.exporter.dot import export_to_pydot
from IPython.display import Image, display


def view_pydot(pdot):
    export_to_pydot(pdot).write_png('./graph.png')


def find_first_spanning_tree(graph: Graph) -> Graph:
    closed = set()
    edges = []

    q = [list(graph.get_vertices())[0]]
    closed.add(q[0])

    while len(q) > 0:
        v = q.pop(0)
        for neighbor in graph.get_neighbors(v):
            if neighbor not in closed:
                closed.add(neighbor)
                edges.append((v, neighbor))
                q.append(neighbor)

    return load_graph_from_set(graph.get_vertices(), edges)


def find_spanning_trees_using_chords(tree: Graph, chords: list[tuple[str, str]]) -> Generator[Graph, None, None]:
    for chord in chords:
        circuit = shortest_path(tree, chord[0], chord[1])
        print('circuit: ', circuit)
        for i in range(len(circuit) - 1):
            edge_to_remove = (circuit[i], circuit[i + 1])
            print('edge to remove: ', edge_to_remove)
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
    tree1 = find_first_spanning_tree(graph)

    view_pydot(tree1)

    print('tree1: ', tree1.get_edges())
    yield tree1

    print('graph: ', graph.get_edges())
    print('tree1: ', tree1.get_edges())

    chords: list[tuple[str, str]] = []
    for edge in graph.get_edges():
        if set(edge) not in map(set, tree1.get_edges()):
            chords.append(edge)

    print('chords: ', chords)

    yield from find_spanning_trees_using_chords(tree1, chords)


V1 = {'A', 'B', 'C', 'D', 'E', 'F'}
E1 = {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
      ('E', 'F'), ('A', 'C'), ('D', 'F')}


def find_n_spanning_trees(graph: Graph, n: int) -> Generator[Graph, None, None]:
    trees = find_spanning_tree(graph)
    for i in range(n):
        yield next(trees)


G1 = load_graph_from_set(V1, E1)

# Find 3 spanning trees in G1

for i, tree in enumerate(find_n_spanning_trees(G1, 3)):
    print(f'Tree {i}: {tree.get_edges()}')
    view_pydot(tree)
    display(Image('./graph.png'))
