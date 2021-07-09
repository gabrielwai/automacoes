from abc import ABC, abstractmethod


class NavegadorAbstractFactory(ABC):

    @abstractmethod
    def criarFireFox(background):
        pass

    @classmethod
    def criarChrome(cls, background):
        pass

    @abstractmethod
    def criarEdge(background):
        pass
