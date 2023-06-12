from src.types.abc_graph import GraphABC


class AMGraph(GraphABC):
    def __init__(self, directed: bool = False):
        super().__init__()
        self.matrix: list[list[int]] = []
        self.translated: dict[str, int] = {}
        self.directed = directed

    def translate(self, vertex: str) -> int:
        return self.translated[vertex]

    def translate_back(self, vertex: int) -> str:
        for key in self.translated:
            if self.translated[key] == vertex:
                return key
        raise ValueError(f"Vertex {vertex} does not exist in graph.")

    def add_vertex(self, vertex: str) -> None:
        if vertex == 'null':
            vertex = str(len(self.matrix))
        self.matrix.append([0] * len(self.matrix))
        for row in self.matrix:
            row.append(0)
        self.translated[vertex] = len(self.matrix) - 1

    def add_edge(self, edge: tuple[str, str]) -> None:
        if edge[0] not in self.translated:
            self.add_vertex(edge[0])
        if edge[1] not in self.translated:
            self.add_vertex(edge[1])
        self.matrix[self.translated[edge[0]]][self.translated[edge[1]]] = 1

        if not self.directed:
            self.matrix[self.translated[edge[1]]][self.translated[edge[0]]] = 1

    def get_vertices(self) -> set[str]:
        return set(self.translated.keys())

    def get_edges(self) -> set[tuple[str, str]]:
        edges = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    edges.add((self.translate_back(i), self.translate_back(j)))
        return edges

    def get_neighbors(self, vertex: str) -> set[str]:
        neighbours = set()
        for i in range(len(self.matrix)):
            if self.matrix[int(vertex)][i] == 1:
                neighbours.add(str(i))
        return neighbours

    def get_vertex(self, vertex: str) -> str:
        for i in range(len(self.matrix)):
            if str(i) == vertex:
                return str(i)

        raise ValueError(f"Vertex {vertex} does not exist in graph.")

    def get_edge(self, edge: tuple[str, str]) -> tuple[str, str]:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    if (str(i), str(j)) == edge:
                        return (str(i), str(j))

        raise ValueError(f"Edge {edge} does not exist in graph.")

    def get_degree(self, vertex: str) -> int:
        return len(self.get_neighbors(vertex))

    def is_directed(self) -> bool:
        return self.directed

    def set_directed(self, is_directed: bool) -> None:
        self.directed = is_directed

    def remove_vertex(self, vertex: str) -> None:
        self.matrix[int(vertex)] = [0 for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            self.matrix[i][int(vertex)] = 0

    def remove_edge(self, edge: tuple[str, str]) -> None:
        self.matrix[int(edge[0])][int(edge[1])] = 0

        if not self.is_directed():
            self.matrix[int(edge[1])][int(edge[0])] = 0

    def get_edges_from_vertex(self, vertex: str) -> set[tuple[str, str]]:
        edges = set()
        for i in range(len(self.matrix)):
            if self.matrix[int(vertex)][i] == 1:
                edges.add((str(i), vertex))
        return edges

    def get_adjacency_matrix(self) -> list[list[int]]:
        return self.matrix

    def is_connected(self) -> bool:
        visited = set()
        stack = [0]

        while stack:
            current = stack.pop()
            visited.add(current)

            for i in range(len(self.matrix)):
                if self.matrix[current][i] == 1 and i not in visited:
                    stack.append(i)

        return len(visited) == len(self.matrix)

    def get_num_vertices(self) -> int:
        return len(self.matrix)

    def get_num_edges(self) -> int:
        return sum([sum(row) for row in self.matrix])
