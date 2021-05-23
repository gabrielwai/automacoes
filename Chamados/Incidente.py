from Chamados.InterfaceStrategy import TiposDeChamados
from Chamados.Chamado import Chamado
from Automacoes.Chamado import *


class Incidente(Chamado, TiposDeChamados):
    def __init__(self, cdIM, SD=None):
        self.__cdIM = cdIM
        super().__init__(SD)
        super().adicionarChamadoRelacionado(cdIM)


    def resolver(self, chamado, ADP, link):
        print('resolvendo chamado...')
        #atualizarChamado(ADP.navegador, self.getIM())
        resolverChamado()


    def atualizarChamado(self, chamado, ADP, link):
        print("atualizado chamado...")


    def designar(self, chamado, ADP, link):
        print('atualizando designado...')


    def getIM(self):
        return self.__cdIM
