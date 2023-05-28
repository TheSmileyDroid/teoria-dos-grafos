class Graph:
    _vertices: set[str]
    _edges: set[tuple[str, str]]
    _is_directed: bool

    def __init__(self, is_directed: bool = False) -> None:
        self._vertices = set()
        self._edges = set()
        self._is_directed = is_directed

    def add_vertex(self, vertex: str) -> None:
        self._vertices.add(vertex)

    def add_edge(self, edge: tuple[str, str]) -> None:
        self._edges.add(edge)

    def get_vertices(self) -> set[str]:
        return self._vertices

    def get_edges(self) -> set[tuple[str, str]]:
        return self._edges

    def get_vertex(self, name: str) -> str:
        for vertex in self._vertices:
            if vertex == name:
                return vertex

        raise ValueError(f"Vertex {name} does not exist in graph.")

    def get_edge(self, name: tuple[str, str]) -> tuple[str, str]:
        for edge in self._edges:
            if edge == name:
                return edge

        raise ValueError(f"Edge {name} does not exist in graph.")

    def get_adjacent_vertices(self, vertex: str) -> set[str]:
        adjacent_vertices: set[str] = set()

        for edge in self._edges:
            if edge[0] == vertex:
                adjacent_vertices.add(edge[1])
            elif edge[1] == vertex:
                adjacent_vertices.add(edge[0])

        return adjacent_vertices

    def get_degree(self, vertex: str) -> int:
        return len(self.get_adjacent_vertices(vertex))

    def is_directed(self) -> bool:
        return self._is_directed

    def __str__(self) -> str:
        return f"Vertices: {self._vertices}\nEdges: {self._edges}"
