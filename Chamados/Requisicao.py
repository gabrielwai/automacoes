from Chamados.ChamadoInterfaceStrategy import TiposDeChamados
from Chamados.Interacao import Interacao
from Automacoes.Chamado import *


class Requisicao(Interacao, TiposDeChamados):
    def __init__(self, cdRF, SD=''):
        self.__cdRF = cdRF
        super().__init__(SD)
        super().adicionarChamadoRelacionado(cdRF)


    def resolver(self, chamado, ADP, link):
        print('resolvendo Requisição...')


    def atualizarChamado(self, chamado, ADP, link):
        print("atualizado Requisição...")


    def designar(self, chamado, ADP, link):
        print('atualizando designado (Requisição)...')


    def getCodigoChamado(self):
        return self.__cdRF
