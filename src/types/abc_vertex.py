from abc import ABC, abstractmethod


class ABCVertex(ABC):
    _name: str
    _edges: set

    def __init__(self, name: str) -> None:
        self._name = name
        self._edges = set()

    @abstractmethod
    def add_edge(self, edge):
        pass

    @abstractmethod
    def get_edges(self) -> set:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
