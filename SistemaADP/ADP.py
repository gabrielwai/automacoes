from Empresas import Empresas
from selenium import webdriver
import Automacoes.ADP


class ADP:
#futuras classes filhas da ADP: menu_full; painel_1 (interface); adm_seg
    def __init__(self, link='https://expert.brasil.adp.com/'):
        self.__link = link
        self.__navegador = webdriver.Chrome()


    def login(self, administrador, empresa):
        verificador = True
        empresa = empresa.strip().upper()
        for emp in Empresas:
            if emp.name in empresa:
                if Automacoes.ADP.login(self.getNavegador(), self.__link, administrador.getUsuario(), administrador.getSenha()):
                    Automacoes.ADP.escolherEmpresa(self.getNavegador(), emp.name)
                    verificador = False
        if verificador:
            print("Erro ao efetuar o login, verifique suas credenciais.")
            exit()
            return False
        else:
            return True


    def getLink(self):
        return self.__link


    def getNavegador(self):
        return self.__navegador


    def resetSenha(self, colaborador):
        if Automacoes.ADP.buscarColaborador(self.getNavegador(), colaborador):
            Automacoes.ADP.resetarSenha(self.getNavegador(), colaborador)
            return True
        else:
            print("Usuário não encontrado para reset de senha:",
                  colaborador.getNome(), colaborador.getEmail(), colaborador.getCpf(),
                  "- empresa:", colaborador.getEmpresa())
            return False
