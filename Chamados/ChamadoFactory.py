from abc import ABC, abstractmethod


class ChamadoFactory(ABC):

    @classmethod
    @abstractmethod
    def novoChamado(cls, codigoChamado):
        pass
