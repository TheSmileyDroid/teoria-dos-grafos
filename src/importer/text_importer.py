import re
from src.structs.graph import Graph


def load_graph_from_string(string: str) -> Graph:
    graph = Graph()

    separators = "[\n;]+"

    lines = re.split(separators, string)
    for line in lines:
        if line.startswith("v"):
            vertex = line[2:]
            graph.add_vertex(vertex)
        elif line.startswith("e"):
            vertices = line[2:].split(" ")
            v1 = graph.get_vertex(vertices[0])
            v2 = graph.get_vertex(vertices[1])
            edge = v1, v2
            graph.add_edge(edge)

    return graph


def load_graph_from_set(vertices: set[str], edges: set[tuple[str, str]]) -> Graph:
    graph = Graph()

    for vertex in vertices:
        graph.add_vertex(vertex)

    for edge in edges:
        graph.add_edge(edge)

    return graph


def load_from_edge_weight(edge_weight: dict[tuple[str, str], int]) -> Graph:
    graph = Graph()

    for edge in edge_weight:
        graph.add_edge(edge)
        graph.add_edge_weight(edge, edge_weight[edge])

    return graph
