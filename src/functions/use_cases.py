from queue import Queue
from src.types.graph import Graph


def view_pydot(graph: Graph):
    pass


def add_greater_edge(graph: Graph, v1: int, sequ: list[int], info: str) -> bool:
    for i, v in enumerate(sequ):
        if i > v1 and v >= sequ[v1]:
            graph.add_vertex(f'{sequ[i]}-{info}')
            graph.add_edge((f'{sequ[i]}-{info}', info))
            return add_greater_edge(graph, i, sequ, f'{sequ[i]}-{info}')
    return True


def maior_caminho(graph: Graph, v1: str) -> str:
    if graph.get_num_edges() != graph.get_num_vertices() - 1:
        raise ValueError('Grafo não é uma árvore')

    q: Queue = Queue()
    visited = set()

    q.put((v1, 0))
    visited.add(v1)

    distances = list[list[str]]()
    while not q.empty():
        vertex, distance = q.get()

        distances.append([vertex, distance])

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                q.put((neighbor, distance + 1))
                visited.add(neighbor)

    return max(distances, key=lambda x: x[1])[0]


def gera_grafo(sequ: list[int]) -> Graph:
    graph = Graph()

    graph.add_vertex('Raiz')
    for i, v in enumerate(sequ):
        graph.add_vertex(str(v))
        graph.add_edge(('Raiz', str(v)))
        add_greater_edge(graph, i, sequ, f'{v}')
    return graph


def monoticamente_crescente(sequ: list[int]) -> str:
    if len(sequ) == 0:
        return 'Raiz'

    graph = gera_grafo(sequ)
    view_pydot(graph)
    return maior_caminho(graph, 'Raiz')


monoticamente_crescente([6, 3, 7, 4, 15, 30, 21, 2, 40, 4])
