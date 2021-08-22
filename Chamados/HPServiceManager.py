import xml.etree.ElementTree as ET
import Automacoes.Chamado


class HPServiceManager:
    def __init__(self, usuario, senha, tipoNavegador, email=None, link='https://app.mapfre.com/smbbex/index.do?lang=pt-Br&mode=index.do&logout_msg=LogoutPage.session_timeout'):
        self.__navegador = None
        self.__link = link
        self.__chamados = set()
        self.__tipoNavegador = tipoNavegador
        self.__usuario, self.__senha, self.__email = usuario, senha, email


        if not Automacoes.Chamado.loginHPServiceManager(self.getNavegador(), self.getLink(), self.getUsuario(), self.getSenha(), statusLogin=True):
            print("Erro ao efetuar o login.")
            exit()


    def getNavegador(self):
        if not bool(self.__navegador):
            self.__navegador = self.__tipoNavegador.criarNavegador()
        return self.__navegador


    def pesquisarChamado(self, chamado):
        chamado = chamado.strip()
        if chamado[0] == "S":
            xpath = '//*[@id="ext-gen-top125"]/span'
        elif chamado[0] == "I":
            xpath = '//*[@id="ext-gen-top173"]'
        else:
            xpath = '//*[@id="ext-gen-top254"]/span'

        Automacoes.Chamado.localizar(chamado, self.__getNavegador, xpath)


    def adicionarChamado(self, SD):
        self.__chamados.add(SD)


    def getChamados(self):
        return self.__chamados


    def getUsuario(self):
        return self.__usuario


    def getSenha(self):
        return self.__senha


    def getEmail(self):
        return self.__email


    def getLink(self):
        return self.__link


    def setUsuario(self, usuario):
        self.__usuario = usuario


    def setSenha(self, senha):
        self.__senha = senha


    def setEmail(self, email):
        self.__email = email


    def transcrever_xml_login(self, arquivoXML):
        with open(arquivoXML, 'r') as arquivo:
            xml = arquivo.read()
            xml = ET.fromstring(xml)
        conta = dict()
        xml.find('colaborador')
        conta['usuario'] = xml[0].text
        conta['senha'] = xml[1].text
        conta['email'] = xml[2].text
        return conta.values()


    def getFormatoXML(self):
        '''
        :return: (string) retorna o formato do arquivo XML suportado pela classe.
        '''
        return "<colaborador>\n\
        <usuario></usuario>\n\
        <senha></senha>\n\
        <email></email>\n\
    </colaborador>"
