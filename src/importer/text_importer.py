from src.types.graph import Graph


def load_graph_from_string(string: str) -> Graph:
    graph = Graph()

    lines = string.split("\n")
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
