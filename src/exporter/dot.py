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
        beautify="true",
    )

    max_weigth = max(graph.get_edge_weights().values())

    for node in graph.get_vertices():
        dot_node = pydot.Node(node)
        dot_graph.add_node(dot_node)
    for edge in graph.get_edges():
        dot_edge = pydot.Edge(edge[0], edge[1], penwidth=str(
            graph.get_edge_weight(edge) * 4 / max_weigth))
        dot_graph.add_edge(dot_edge)
    return dot_graph
