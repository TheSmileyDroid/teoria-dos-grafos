from vertex import Vertex
from edge import Edge


class Graph:
    _vertices: set[Vertex]
    _edges: set[Edge]

    def __init__(self) -> None:
        self._vertices = set()
        self._edges = set()

    def add_vertex(self, vertex: Vertex) -> None:
        self._vertices.add(vertex)

    def add_edge(self, edge: Edge) -> None:
        self._edges.add(edge)

    def get_vertices(self) -> set[Vertex]:
        return self._vertices

    def get_edges(self) -> set[Edge]:
        return self._edges

    def get_vertex(self, name: str) -> Vertex:
        for vertex in self._vertices:
            if vertex.get_name() == name:
                return vertex

        raise ValueError(f"Vertex {name} does not exist in graph.")

    def get_edge(self, name: str) -> Edge:
        for edge in self._edges:
            if edge.get_name() == name:
                return edge

        raise ValueError(f"Edge {name} does not exist in graph.")

    def __str__(self) -> str:
        return f"Vertices: {self._vertices}\nEdges: {self._edges}"
