import pydot  # type: ignore
from src.structs.graph import Graph


def export_to_pydot(graph: Graph) -> pydot.Dot:
    dot_graph = pydot.Dot(
        graph_type="digraph" if graph.is_directed() else "graph",
        splines="true",
        overlap="false",
        concentrate="true",
        nodesep="0.1",
        layout="sfdp",
        beautify="false",
    )

    max_weigth = 1

    if len(graph.get_edge_weights().values()) != 0:
        max_weigth = max(graph.get_edge_weights().values())
    if max_weigth < 1:
        max_weigth = 1

    for node in graph.get_vertices():
        dot_node = pydot.Node(node)
        dot_graph.add_node(dot_node)
    for edge in graph.get_edges():
        peso = graph.get_edge_weight(edge)**2 / max_weigth
        if peso < 0.1:
            peso = 0.1
        if peso > 4:
            peso = 4
        dot_edge = pydot.Edge(edge[0], edge[1], penwidth=str(peso))
        dot_graph.add_edge(dot_edge)
    return dot_graph
