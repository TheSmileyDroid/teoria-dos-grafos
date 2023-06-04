import unittest
from src.types.graph import Graph
from src.functions.paths import shortest_path


class TestShortestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_vertex("D")
        self.graph.add_vertex("E")
        self.graph.add_edge(("A", "B"))
        self.graph.add_edge(("B", "C"))
        self.graph.add_edge(("D", "A"))

    def test_shortest_path(self) -> None:
        self.assertEqual(shortest_path(self.graph, "A", "C"), ["A", "B", "C"])
        self.assertEqual(shortest_path(self.graph, "A", "D"), ["A", "D"])
        self.assertEqual(shortest_path(self.graph, "B", "D"), ["B", "A", "D"])
        self.assertEqual(shortest_path(
            self.graph, "D", "C"), ["D", "A", "B", "C"])
        self.assertEqual(shortest_path(self.graph, "A", "E"), [])

    def test_shortest_path_single_vertex(self) -> None:
        graph = Graph()
        graph.add_vertex("A")
        self.assertEqual(shortest_path(graph, "A", "A"), ["A"])

    def test_shortest_path_unreachable_vertex(self) -> None:
        self.assertEqual(shortest_path(self.graph, "A", "E"), [])

    def test_shortest_path_same_start_and_end(self) -> None:
        self.assertEqual(shortest_path(self.graph, "A", "A"), ["A"])

    def test_shortest_path_invalid_start_vertex(self) -> None:
        with self.assertRaises(ValueError):
            shortest_path(self.graph, "F", "A")

    def test_shortest_path_invalid_end_vertex(self) -> None:
        with self.assertRaises(ValueError):
            shortest_path(self.graph, "A", "F")


if __name__ == "__main__":
    unittest.main()
