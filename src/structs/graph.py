from src.structs.abc_graph import GraphABC


class Graph(GraphABC):
    _vertices: set[str]
    _edges: set[tuple[str, str]]
    _is_directed: bool
    _edge_weights: dict[tuple[str, str], int]

    def __init__(self, is_directed: bool = False) -> None:
        self._vertices = set()
        self._edges = set()
        self._is_directed = is_directed
        self._edge_weights = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex == 'null':
            vertex = str(len(self._vertices))
        self._vertices.add(vertex)

    def add_edge(self, edge: tuple[str, str]) -> None:
        self._edges.add(edge)
        if edge[0] not in self._vertices:
            self.add_vertex(edge[0])
        if edge[1] not in self._vertices:
            self.add_vertex(edge[1])
        self.add_edge_weight(edge, 1)

    def add_edge_weight(self, edge: tuple[str, str], weight: int) -> None:
        self._edge_weights[edge] = weight

    def get_edge_weight(self, edge: tuple[str, str]) -> int:
        return self._edge_weights[edge] if edge in self._edge_weights else 1

    def get_edge_weights(self) -> dict[tuple[str, str], int]:
        return self._edge_weights

    def remove_vertex(self, vertex_name: str) -> None:
        self._vertices.remove(self.get_vertex(vertex_name))

        for edge in self.get_edges_from_vertex(vertex_name):
            self.remove_edge(edge)

    def remove_edge(self, edge: tuple[str, str]) -> None:
        self._edges.remove(self.get_edge(edge))

    def get_vertices(self) -> set[str]:
        return self._vertices

    def get_edges(self) -> set[tuple[str, str]]:
        return self._edges

    def get_edges_from_vertex(self, vertex: str) -> set[tuple[str, str]]:
        edges = set()
        for edge in self._edges:
            if edge[0] == vertex or edge[1] == vertex:
                edges.add(edge)
        return edges

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

    def get_neighbors(self, vertex: str) -> set[str]:
        neighbours = set()
        for edge in self._edges:
            if edge[0] == vertex:
                neighbours.add(edge[1])
            elif edge[1] == vertex:
                neighbours.add(edge[0])
        return neighbours

    def get_degree(self, vertex: str) -> int:
        return len(self.get_neighbors(vertex))

    def is_directed(self) -> bool:
        return self._is_directed

    def get_num_vertices(self) -> int:
        return len(self._vertices)

    def get_num_edges(self) -> int:
        return len(self._edges)

    def set_directed(self, is_directed: bool) -> None:
        self._is_directed = is_directed

    def is_connected(self) -> bool:
        visited = set()
        stack = [list(self._vertices)[0]]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                for adjacent in self.get_neighbors(vertex):
                    stack.append(adjacent)

        return len(visited) == len(self._vertices)

    def __str__(self) -> str:
        return f"Vertices: {self._vertices}\nEdges: {self._edges}\nDirected: {self._is_directed}"
