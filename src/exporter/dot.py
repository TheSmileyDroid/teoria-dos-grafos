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
        peso = float(graph.get_edge_weight(edge)**2)
        # keep size between 1 and 6
        peso = (((peso - 1) * (6 - 1)) / (max_weigth**2 - 1)) + 1

        dot_edge = pydot.Edge(edge[0], edge[1], penwidth=str(peso))
        dot_graph.add_edge(dot_edge)
    return dot_graph
