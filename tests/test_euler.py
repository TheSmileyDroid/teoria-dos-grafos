import unittest
from src.types.graph import Graph
from src.functions.euler import is_euler_graph


class TestEuler(unittest.TestCase):
    def test_is_euler_graph_connected(self):
        # Test a connected graph with all even degree vertices
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'A'))
        self.assertEqual(is_euler_graph(graph), True)

    def test_is_euler_graph_disconnected(self):
        # Test a disconnected graph with all even degree vertices
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('C', 'D'))
        self.assertEqual(is_euler_graph(graph), False)

    def test_is_euler_graph_odd_degree(self):
        # Test a connected graph with an odd degree vertex
        graph = Graph()
        graph.add_edge(('A', 'B'))
        graph.add_edge(('B', 'C'))
        graph.add_edge(('C', 'D'))
        graph.add_edge(('D', 'A'))
        graph.add_edge(('A', 'E'))
        self.assertEqual(is_euler_graph(graph), False)

    def test_is_euler_graph_self_loop(self):
        # Test a graph with a self-loop
        graph = Graph()
        graph.add_edge(('A', 'A'))
        self.assertEqual(is_euler_graph(graph), False)


if __name__ == '__main__':
    unittest.main()
