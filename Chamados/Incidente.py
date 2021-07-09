import Automacoes.Chamado
from Chamados.ChamadoInterfaceStrategy import TiposDeChamados
from Chamados.Interacao import Interacao


class Incidente(Interacao, TiposDeChamados):
    def __init__(self, cdIM, SD=''):
        self.__xpath = '//*[@id="ext-gen-top172"]'
        self.__cdIM = cdIM
        super().__init__(SD)
        super().adicionarChamadoRelacionado(cdIM)


    def resolver(self, chamado, ADP, link):
        print('resolvendo Incidente...')


    def atualizarChamado(self, chamado, ADP, link):
        print("atualizado Incidente...")


    def designar(self, chamado, ADP, link):
        print('atualizando designado (Incidente)...')


    def localizarChamado(self, HPServiceManager):
        Automacoes.Chamado.localizar(self.getCodigoChamado(), HPServiceManager.getNavegador(), self.__xpath)


    def getCodigoChamado(self):
        return self.__cdIM
