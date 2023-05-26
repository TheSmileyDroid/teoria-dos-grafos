from abc_edge import ABCEdge
from abc_vertex import ABCVertex


class Edge(ABCEdge):
    _weight: int
    _vertices: tuple[ABCVertex, ABCVertex]
    _bidirectional: bool
    _name: str

    def __init__(
        self,
        vertex1: ABCVertex,
        vertex2: ABCVertex,
        weight: int = 1,
        bidirectional: bool = True,
        name: str = "",
    ) -> None:
        self._weight = weight
        self._vertices = (vertex1, vertex2)
        self._bidirectional = bidirectional
        self._name = name

        vertex1.add_edge(self)
        vertex2.add_edge(self)

    def get_weight(self) -> int:
        return self._weight

    def get_vertices(self) -> tuple[ABCVertex, ABCVertex]:
        return self._vertices

    def is_bidirectional(self) -> bool:
        return self._bidirectional

    def get_name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"({self._vertices[0]}, {self._vertices[1]})"

    def __repr__(self) -> str:
        return f"({self._vertices[0]}, {self._vertices[1]})"
