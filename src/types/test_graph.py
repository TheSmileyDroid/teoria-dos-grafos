import unittest
from vertex import Vertex
from edge import Edge
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_add_vertex(self) -> None:
        v1 = Vertex("A")
        self.graph.add_vertex(v1)
        self.assertIn(v1, self.graph.get_vertices())

    def test_add_edge(self) -> None:
        v1 = Vertex("A")
        v2 = Vertex("B")
        e1 = Edge(v1, v2)
        self.graph.add_edge(e1)
        self.assertIn(e1, self.graph.get_edges())

    def test_get_vertices(self) -> None:
        v1 = Vertex("A")
        v2 = Vertex("B")
        self.graph.add_vertex(v1)
        self.graph.add_vertex(v2)
        vertices: set[Vertex] = self.graph.get_vertices()
        self.assertIn(v1, vertices)
        self.assertIn(v2, vertices)

    def test_get_edges(self) -> None:
        v1 = Vertex("A")
        v2 = Vertex("B")
        e1 = Edge(v1, v2)
        self.graph.add_edge(e1)
        edges = self.graph.get_edges()
        self.assertIn(e1, edges)

    def test_str(self) -> None:
        v1 = Vertex("A")
        v2 = Vertex("B")
        e1 = Edge(v1, v2)
        self.graph.add_vertex(v1)
        self.graph.add_vertex(v2)
        self.graph.add_edge(e1)
        expected_str = "Vertices: {A, B}\nEdges: {(A, B)}"
        self.assertEqual(str(self.graph), expected_str)


if __name__ == "__main__":
    unittest.main()
