import unittest
from src.types.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_add_vertex(self) -> None:
        v1 = "A"
        self.graph.add_vertex(v1)
        self.assertIn(v1, self.graph.get_vertices())

    def test_add_edge(self) -> None:
        v1 = "A"
        v2 = "B"
        e1 = v1, v2
        self.graph.add_edge(e1)
        self.assertIn(e1, self.graph.get_edges())

    def test_get_vertices(self) -> None:
        v1 = "A"
        v2 = "B"
        self.graph.add_vertex(v1)
        self.graph.add_vertex(v2)
        vertices: set[str] = self.graph.get_vertices()
        self.assertIn(v1, vertices)
        self.assertIn(v2, vertices)

    def test_get_edges(self) -> None:
        v1 = "A"
        v2 = "B"
        e1 = v1, v2
        self.graph.add_edge(e1)
        edges = self.graph.get_edges()
        self.assertIn(e1, edges)

    def test_get_vertex(self) -> None:
        v1 = "A"
        self.graph.add_vertex(v1)
        self.assertEqual(self.graph.get_vertex(v1), v1)

    def test_get_vertex_not_found(self) -> None:
        with self.assertRaises(ValueError):
            self.graph.get_vertex("A")


if __name__ == "__main__":
    unittest.main()
