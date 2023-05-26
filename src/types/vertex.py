from abc_edge import ABCEdge
from abc_vertex import ABCVertex


class Vertex(ABCVertex):
    _name: str
    _edges: set[ABCEdge]

    def __init__(self, name: str) -> None:
        self._name = name
        self._edges = set()

    def add_edge(self, edge: ABCEdge) -> None:
        self._edges.add(edge)

    def get_edges(self) -> set[ABCEdge]:
        return self._edges

    def get_name(self) -> str:
        return self._name

    def get_adjacent(self) -> set[ABCVertex]:
        adjacent = set()
        for edge in self._edges:
            if edge.get_vertices()[0] == self:
                adjacent.add(edge.get_vertices()[1])
            else:
                adjacent.add(edge.get_vertices()[0])
        return adjacent

    def get_degree(self) -> int:
        return len(self._edges)

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self._name
