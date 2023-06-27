import unittest
from src.types.am_graph import AMGraph
from src.types.graph import Graph
from src.functions.tree import (
    is_tree,
    distance_between_vertices,
    eccentricity,
    tree_center,
)


class TestTree(unittest.TestCase):
    def test_is_tree_connected(self):
        # Test a connected tree
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        self.assertTrue(is_tree(graph))

        # Test a connected graph that is not a tree
        graph.add_edge(('E', 'A'))
        self.assertFalse(is_tree(graph))

        # Test a disconnected graph that is not a tree
        graph.remove_edge(('E', 'A'))
        graph.add_vertex('F')
        self.assertFalse(is_tree(graph))

    def test_is_tree_edges(self):
        # Test a tree with n-1 edges
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        self.assertTrue(is_tree(graph))

        # Test a tree with less than n-1 edges
        graph.remove_edge(('D', 'E'))
        self.assertFalse(is_tree(graph))

        # Test a tree with more than n-1 edges
        graph.add_edge(('E', 'F'))
        self.assertFalse(is_tree(graph))

        # Test a disconnected graph with n-1 edges
        graph.remove_edge(('E', 'F'))
        graph.add_vertex('F')
        self.assertFalse(is_tree(graph))

    def test_is_tree_am_matrix(self):
        # Test a tree with n-1 edges
        graph = AMGraph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        self.assertTrue(graph.is_connected())
        self.assertEqual(graph.get_num_edges(), 4)
        self.assertEqual(graph.get_num_vertices(), 5)

        self.assertTrue(is_tree(graph))

    def test_distance_between_vertices(self):
        # Test the distance between two adjacent vertices
        graph = Graph()
        graph.add_edge(('A', 'B'))
        self.assertEqual(distance_between_vertices(graph, 'A', 'B'), 1)

        # Test the distance between two vertices in a longer path
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        self.assertEqual(distance_between_vertices(graph, 'A', 'E'), 4)

        # Test the distance between two vertices in a disconnected graph
        graph.add_vertex('F')
        self.assertEqual(distance_between_vertices(graph, 'A', 'F'), -1)

    def test_eccentricity(self):
        # Test the eccentricity of a vertex in a disconnected graph
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        graph.add_vertex('F')
        self.assertEqual(eccentricity(graph, 'A'), 4)
        self.assertEqual(eccentricity(graph, 'F'), 0)
        self.assertEqual(eccentricity(graph, 'C'), 2)

    def test_tree_center(self):
        # Test the center of a tree with an odd number of vertices
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'E'))
        self.assertEqual(tree_center(graph), ['C'])

        # Test the center of a tree with an even number of vertices
        graph.remove_vertex('E')
        self.assertEqual(set(tree_center(graph)), set(['B', 'C']))

        # Test the center of a disconnected graph
        graph.add_vertex('F')
        self.assertRaises(ValueError, tree_center, graph)


if __name__ == '__main__':
    unittest.main()
