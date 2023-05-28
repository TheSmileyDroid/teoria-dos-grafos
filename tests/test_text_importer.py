import unittest
from src.importer.text_importer import load_graph_from_string, Graph


class TestTextImporter(unittest.TestCase):
    def test_load_graph_from_string_empty(self):
        string = ""
        graph = load_graph_from_string(string)
        self.assertIsInstance(graph, Graph)
        self.assertEqual(len(graph.get_vertices()), 0)
        self.assertEqual(len(graph.get_edges()), 0)

    def test_load_graph_from_string_single_vertex(self):
        string = "v 1\n"
        graph = load_graph_from_string(string)
        self.assertIsInstance(graph, Graph)
        self.assertEqual(len(graph.get_vertices()), 1)
        self.assertEqual(len(graph.get_edges()), 0)
        self.assertIn("1", graph.get_vertices())

    def test_load_graph_from_string_single_edge(self):
        string = "v 1\nv 2\ne 1 2\n"
        graph = load_graph_from_string(string)
        self.assertIsInstance(graph, Graph)
        self.assertEqual(len(graph.get_vertices()), 2)
        self.assertEqual(len(graph.get_edges()), 1)
        self.assertIn("1", graph.get_vertices())

    def test_load_graph_from_string_multiple_edges(self):
        string = "v 1\nv 2\nv 3\ne 1 2\ne 2 3\n"
        graph = load_graph_from_string(string)
        self.assertIsInstance(graph, Graph)
        self.assertEqual(len(graph.get_vertices()), 3)
        self.assertEqual(len(graph.get_edges()), 2)
        self.assertIn("1", graph.get_vertices())
        self.assertIn("2", graph.get_vertices())
        self.assertIn("3", graph.get_vertices())
        self.assertIn(("1", "2"), graph.get_edges())
        self.assertIn(("2", "3"), graph.get_edges())


if __name__ == "__main__":
    unittest.main()
