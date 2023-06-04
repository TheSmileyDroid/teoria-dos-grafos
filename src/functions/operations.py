from src.types.graph import Graph


def union(graph1: Graph, graph2: Graph) -> Graph:
    union_graph = Graph()

    union_graph._vertices = graph1.get_vertices().union(graph2.get_vertices())
    union_graph._edges = graph1.get_edges().union(graph2.get_edges())

    return union_graph


def intersection(graph1: Graph, graph2: Graph) -> Graph:
    intersection_graph = Graph()

    intersection_graph._vertices = graph1.get_vertices().intersection(
        graph2.get_vertices()
    )

    intersection_graph._edges = graph1.get_edges().intersection(
        graph2.get_edges()
    )

    return intersection_graph


def symmetric_difference(graph1: Graph, graph2: Graph) -> Graph:
    symmetric_difference_graph = Graph()

    symmetric_difference_graph._vertices = graph1.get_vertices().symmetric_difference(  # noqa E501
        graph2.get_vertices()
    )

    symmetric_difference_graph._edges = graph1.get_edges().symmetric_difference(  # noqa E501
        graph2.get_edges()
    )

    edges_for_removal = set()

    for edge in symmetric_difference_graph._edges:
        if (
            edge[0] not in symmetric_difference_graph._vertices
            or edge[1] not in symmetric_difference_graph._vertices
        ):
            edges_for_removal.add(edge)

    print(edges_for_removal)
    print(symmetric_difference_graph._vertices)

    for edge in edges_for_removal:
        symmetric_difference_graph._edges.remove(edge)

    return symmetric_difference_graph


def remove_vertex(graph: Graph, vertex_name: str) -> Graph:
    new_graph = Graph()

    new_graph._vertices = graph.get_vertices().copy()
    new_graph._edges = graph.get_edges().copy()

    new_graph._vertices.remove(graph.get_vertex(vertex_name))

    for edge in graph.get_edges():
        if edge[0] == vertex_name or edge[1] == vertex_name:
            new_graph._edges.remove(edge)

    return new_graph


def remove_edge(graph: Graph, edge: tuple[str, str]) -> Graph:
    new_graph = Graph()

    new_graph._vertices = graph.get_vertices().copy()
    new_graph._edges = graph.get_edges().copy()

    edge = graph.get_edge(edge)

    new_graph._edges.remove(edge)

    return new_graph


def fuse_vertices(graph: Graph, vertex1: str, vertex2: str) -> Graph:
    new_graph = Graph()

    new_graph._vertices = graph.get_vertices().copy()
    new_graph._edges = graph.get_edges().copy()

    vertex1 = graph.get_vertex(vertex1)
    vertex2 = graph.get_vertex(vertex2)

    new_graph._vertices.remove(vertex1)
    new_graph._vertices.remove(vertex2)

    new_vertex = vertex1 + vertex2

    new_graph._vertices.add(new_vertex)

    for edge in graph.get_edges():
        if edge[0] == vertex1 or edge[0] == vertex2:
            new_graph._edges.remove(edge)
            if edge[1] != vertex1 and edge[1] != vertex2:
                new_graph._edges.add((new_vertex, edge[1]))
            else:
                new_graph._edges.add((new_vertex, new_vertex))
        elif edge[1] == vertex1 or edge[1] == vertex2:
            new_graph._edges.remove(edge)
            if edge[0] != vertex1 and edge[0] != vertex2:
                new_graph._edges.add((edge[0], new_vertex))
            else:
                new_graph._edges.add((new_vertex, new_vertex))

    return new_graph


def intersecting(graph1: Graph, graph2: Graph) -> Graph:
    intersecting_graph = Graph()

    intersecting_graph._vertices = graph1.get_vertices().intersection(
        graph2.get_vertices()
    )

    intersecting_graph._edges = graph1.get_edges().intersection(
        graph2.get_edges()
    )

    return intersecting_graph
