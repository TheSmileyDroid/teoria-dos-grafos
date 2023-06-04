from abc import ABC, abstractmethod


class GraphABC(ABC):
    @abstractmethod
    def get_vertices(self) -> set:
        pass

    @abstractmethod
    def get_edges(self) -> set:
        pass

    @abstractmethod
    def get_neighbours(self, vertex: str) -> set:
        pass

    @abstractmethod
    def get_vertex(self, vertex: str) -> str:
        pass

    @abstractmethod
    def get_edge(self, edge: tuple[str, str]) -> tuple[str, str]:
        pass

    @abstractmethod
    def get_degree(self, vertex: str) -> int:
        pass

    @abstractmethod
    def get_num_vertices(self) -> int:
        pass

    @abstractmethod
    def get_num_edges(self) -> int:
        pass

    @abstractmethod
    def is_directed(self) -> bool:
        pass

    @abstractmethod
    def add_vertex(self, vertex: str) -> None:
        pass

    @abstractmethod
    def add_edge(self, edge: tuple[str, str]) -> None:
        pass

    @abstractmethod
    def set_directed(self, is_directed: bool) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass
