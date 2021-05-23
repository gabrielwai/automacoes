from Chamados.Chamado import Chamado


class Requisicao(Chamado):
    def __init__(self, cdRF, SD=None):
        self.__cdRF = cdRF
        super().__init__(SD)
        super().adicionarChamadoRelacionado(cdRF)
