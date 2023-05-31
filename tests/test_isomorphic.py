import unittest
from src.types.graph import Graph
from src.functions.isomorphic import is_isomorphic


class TestIsomorphic(unittest.TestCase):
    def setUp(self) -> None:
        self.graph1 = Graph()
        self.graph2 = Graph()

    def test_is_isomorphic_directed(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_edge(("A", "B"))

        self.assertTrue(is_isomorphic(self.graph1, self.graph2))

    def test_is_isomorphic_undirected(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_edge(("B", "A"))

        self.assertTrue(is_isomorphic(self.graph1, self.graph2))

    def test_is_not_isomorphic_undirected(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_edge(("A", "B"))
        self.graph2.add_edge(("B", "A"))

        self.assertFalse(is_isomorphic(self.graph1, self.graph2))

    def test_is_not_isomorphic_different_num_vertices(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")

        self.assertFalse(is_isomorphic(self.graph1, self.graph2))

    def test_is_not_isomorphic_different_num_edges(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_edge(("A", "B"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")
        self.graph2.add_edge(("A", "B"))

        self.assertFalse(is_isomorphic(self.graph1, self.graph2))

    def test_is_not_isomorphic_different_degree_sequence(self) -> None:
        self.graph1.add_vertex("A")
        self.graph1.add_vertex("B")
        self.graph1.add_vertex("C")
        self.graph1.add_edge(("A", "B"))
        self.graph1.add_edge(("B", "C"))

        self.graph2.add_vertex("A")
        self.graph2.add_vertex("B")
        self.graph2.add_vertex("C")
        self.graph2.add_edge(("A", "B"))
        self.graph2.add_edge(("B", "C"))
        self.graph2.add_edge(("C", "A"))

        self.assertFalse(is_isomorphic(self.graph1, self.graph2))


if __name__ == "__main__":
    unittest.main()
