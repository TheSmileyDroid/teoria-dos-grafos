import unittest
from src.structs.graph import Graph
from src.functions.subgraph import (
    is_subgraph,
    is_graph_vertex_disjoint,
    is_graph_edge_disjoint,
)


class TestSubgraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph1 = Graph()
        self.graph2 = Graph()

    def test_is_subgraph_directed(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))
        self.graph1.add_edge(("B", "A"))
        self.graph1.set_directed(True)

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_edge(("A", "B"))
        self.graph2.set_directed(True)

        self.assertTrue(is_subgraph(self.graph1, self.graph2))

    def test_is_subgraph_undirected(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))
        self.graph1.add_edge(("B", "A"))
        self.graph1.set_directed(False)

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_edge(("A", "B"))
        self.graph2.set_directed(False)

        self.assertTrue(is_subgraph(self.graph1, self.graph2))

    def test_is_subgraph_not_subgraph(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))
        self.graph1.set_directed(True)

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")
        self.graph2.add_edge(("A", "B"))
        self.graph2.add_edge(("B", "C"))
        self.graph2.set_directed(True)

        self.assertFalse(is_subgraph(self.graph1, self.graph2))

    def test_is_graph_vertex_disjoint(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")

        self.graph2.add_vertex("C")
        self.graph2.add_vertex("D")

        self.assertTrue(is_graph_vertex_disjoint(self.graph1, self.graph2))

    def test_is_graph_vertex_not_disjoint(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")

        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")

        self.assertFalse(is_graph_vertex_disjoint(self.graph1, self.graph2))

    def test_is_graph_edge_disjoint(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("C")
        self.graph2.add_vertex("D")
        self.graph2.add_edge(("C", "D"))

        self.assertTrue(is_graph_edge_disjoint(self.graph1, self.graph2))

    def test_is_graph_edge_not_disjoint(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")
        self.graph2.add_edge(("A", "B"))

        self.assertFalse(is_graph_edge_disjoint(self.graph1, self.graph2))


if __name__ == "__main__":
    unittest.main()
