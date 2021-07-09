from Chrome import Chrome
from Navegador import Navegador
from NavegadorFactory import NavegadorFactory
from Autentificador import Autentificador
from Empresas import Empresas
import Automacoes.ADP


class ADP:
#futuras classes filhas da ADP: menu_full; painel_1 (interface); adm_seg
    def __init__(self, tipoNavegador, link='https://expert.brasil.adp.com/', backgorund=True):
        self.__backgorund = bool(backgorund)
        self.__navegador = None
        self.__link = link
        self.__tipoNavegador = tipoNavegador


    def login(self, administrador, empresa):
        verificador = True

        if not Autentificador(administrador.getUsuario(), administrador.getSenha()):
            print('Insira o login para acesso ao sistema ADP no arquivo xml destinado ao administrador.')
            print('Falha ao realizar o login no sistema ADP.'); exit()

        empresa = empresa.strip().upper()
        for emp in Empresas:
            if emp.name in empresa:
                if Automacoes.ADP.login(self.__getNavegador(), self.getLink(), administrador.getUsuario(), administrador.getSenha()):
                    Automacoes.ADP.escolherEmpresa(self.__getNavegador(), emp.name)
                    verificador = False
        if verificador:
            print("Erro ao efetuar o login, verifique a resposta do navegador e suas credenciais de acesso.")
            exit()
        else:
            return True


    def getLink(self):
        return self.__link


    def isbackgorund(self):
        return self.__backgorund


    def setBackground(self, backgorund):
        backgorund = bool(backgorund)
        self.__backgorund = backgorund


    def __getNavegador(self):
        if not bool(self.__navegador):
            self.__navegador = self.__tipoNavegador.criarNavegador()
        return self.__navegador


    def resetSenha(self, colaborador):
        if Automacoes.ADP.buscarColaborador(self.__getNavegador(), colaborador):
            if Automacoes.ADP.resetarSenha(self.__getNavegador()):
                return True
            else:
                print('Mais de um colaborador foi encontrado, '
                      'cancelando operação de reset de senha...')
                return False
        else:
            print("Usuário não encontrado para reset de senha:",
                  colaborador.getNome(), colaborador.getEmail(), colaborador.getCpf(),
                  "- empresa:", colaborador.getEmpresa())
            return False

    def getTesteNavegador(self):
        return self.__getNavegador()
