from src.types.abc_graph import Graph


class AMGraph(Graph):
    def __init__(self, num_vertices: int, directed: bool = False):
        super().__init__()
        self.matrix = [[0 for _ in range(num_vertices)]
                       for _ in range(num_vertices)]

    def add_edge(self, edge: tuple[str, str]) -> None:
        self.matrix[int(edge[0])][int(edge[1])] = 1

        if not self.is_directed():
            self.matrix[int(edge[1])][int(edge[0])] = 1

    def get_vertices(self) -> set[str]:
        return set([str(i) for i in range(len(self.matrix))])

    def get_edges(self) -> set[tuple[str, str]]:
        edges = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    edges.add((str(i), str(j)))
        return edges

    def get_neighbours(self, vertex: str) -> set[str]:
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
        return len(self.get_neighbours(vertex))
