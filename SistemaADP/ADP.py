from sqlite3.dbapi2 import connect
from NavegadorFactory import NavegadorFactory
from Empresas import Empresas
import Automacoes.ADP
from sqlite3 import Connection
#import sqlite3


class ADP:
#futuras classes filhas da ADP: menu_full; painel_1 (interface); adm_seg
    def __init__(self, tipoNavegador, link='https://expert.brasil.adp.com/', backgorund=True):
        self.__backgorund = bool(backgorund)
        self.__navegador = None
        self.__link = link
        self.__tipoNavegador = tipoNavegador


    def banco(self):
        #conn = connect('C:/Users/Gabri/Downloads/sqlite/sqlite-tools-win32-x86-3360000/jfmartins-adp.db')
        conn = connect('./sqlite/jfmartins-adp.db')
        curs = conn.cursor()

        #curs.execute("insert into contas values ('usuario_3', 'senha_3', 'BRASILSEG');")
        #conn.commit()

        curs.execute("select * from contas;")
        for usuario, senha, empresa in curs.fetchall():
            print(usuario, senha, empresa)
        

        conn.close()


    def login(self, usuario, senha, empresa):
        verificador = True

        if Automacoes.ADP.login(self.__getNavegador(), self.getLink(), usuario, senha):
            Automacoes.ADP.escolherEmpresa(self.__getNavegador(), empresa)
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
        self.__getNavegador().get('https://www.google.com.br')
        return self.__getNavegador()
