from abc import ABC, abstractmethod


class ABCEdge(ABC):
    _weight: int
    _vertices: tuple
    _bidirectional: bool
    _name: str

    @abstractmethod
    def __init__(
        self,
        vertex1,
        vertex2,
        weight=1,
        bidirectional=True,
        name="",
    ) -> None:
        pass

    @abstractmethod
    def get_vertices(self) -> tuple:
        pass
