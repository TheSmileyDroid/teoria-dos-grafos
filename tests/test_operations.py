import unittest
from src.types.graph import Graph
from src.importer.text_importer import load_graph_from_string
from src.functions.operations import (
    fuse_vertices,
    union,
    intersection,
    symmetric_difference,
    remove_vertex,
    remove_edge,
)


class TestOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.graph1: Graph = load_graph_from_string(
            "v A\nv B\nv C\ne A B\ne B C")

        self.graph2: Graph = load_graph_from_string("v B\nv C\nv D\ne B C")

    def test_union(self) -> None:
        union_graph = union(self.graph1, self.graph2)

        self.assertEqual(union_graph.get_vertices(), {"A", "B", "C", "D"})
        self.assertEqual(union_graph.get_edges(), {("A", "B"), ("B", "C")})

    def test_intersection(self) -> None:
        intersection_graph = intersection(self.graph1, self.graph2)

        self.assertEqual(intersection_graph.get_vertices(), {"B", "C"})
        self.assertEqual(intersection_graph.get_edges(), {("B", "C")})

    def test_symmetric_difference(self) -> None:
        symmetric_difference_graph = symmetric_difference(
            self.graph1,
            self.graph2)

        self.assertEqual(symmetric_difference_graph.get_vertices(), {"A", "D"})
        self.assertEqual(symmetric_difference_graph.get_edges(), set())

    def test_remove_vertex(self) -> None:
        new_graph = remove_vertex(self.graph1, "B")

        self.assertEqual(new_graph.get_vertices(), {"A", "C"})
        self.assertEqual(new_graph.get_edges(), set())

    def test_remove_edge(self):
        new_graph = remove_edge(self.graph1, ("B", "C"))

        self.assertEqual(new_graph.get_vertices(), {"A", "B", "C"})
        self.assertEqual(new_graph.get_edges(), {("A", "B")})

    def test_fuse_vertices(self):
        new_graph = fuse_vertices(self.graph1, "A", "B")

        self.assertEqual(new_graph.get_vertices(), {"AB", "C"})
        self.assertEqual(new_graph.get_edges(), {("AB", "C"), ("AB", "AB")})

        new_graph = fuse_vertices(new_graph, "AB", "C")

        self.assertEqual(new_graph.get_vertices(), {"ABC"})
        self.assertEqual(new_graph.get_edges(), {("ABC", "ABC")})


if __name__ == "__main__":
    unittest.main()
