from abc import ABC, abstractmethod


class Navegador(ABC):

    def __init__(self):
        self._navegador = None


    @abstractmethod
    def criarNavegador(self):
        pass


    def _getNavegador(self):
        # if not bool(self._navegador):
        #     self.criarNavegador()
        # else:
        return self._navegador


    def setOptions(self, options):
        self._options = options


    def _getOptions(self):
        return self._options
