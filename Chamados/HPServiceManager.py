import xml.etree.ElementTree as ET
from selenium import webdriver
import Automacoes.Chamado


class HPServiceManager:
    def __init__(self, link='https://app.mapfre.com/smbbex/index.do?lang=pt-Br&mode=index.do&logout_msg=LogoutPage.session_timeout',
                 arquivoXML='Chamados/loginHPServiceManager.xml'):
        self.__link = link
        self.__chamados = set()
        self.__usuario, self.__senha, self.__email = self.transcrever_xml_login(arquivoXML)
        self.__navegador = webdriver.Chrome()


    def login(self):
        if not Autentificador(self.getUsuario(), self.getSenha()):
            print('Insira o login para acesso ao sistema HP Service Manager no respectivo arquivo xml.')
            print('Falha ao realizar o login no sistema HP Service Manager.'); exit()

        if Automacoes.Chamado.loginHPServiceManager(self.getNavegador(), self.getLink(), self.getUsuario(), self.getSenha(), statusLogin=True):
            return True
        else:
            print("Erro ao efetuar o login.")
            return False


    def adicionarChamado(self, SD):
        self.__chamados.add(SD)


    def getChamados(self):
        return self.__chamados


    def getNavegador(self):
        return self.__navegador


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
