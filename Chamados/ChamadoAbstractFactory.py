from abc import ABC, abstractmethod


class ChamadoAbtractFactory(ABC):

    @staticmethod
    @abstractmethod
    def novoChamado(codigoChamado):
        pass
