from abc import ABC, abstractmethod


class TiposDeChamados(ABC):

    @abstractmethod
    def atualizarChamado(self, chamado, ADP, HPServiceManager):
        pass

    @abstractmethod
    def designar(self, chamado, ADP, HPServiceManager):
        pass

    @abstractmethod
    def resolver(self, chamado, ADP, HPServiceManager):
        pass

    @abstractmethod
    def getCodigoChamado(self):
        pass
