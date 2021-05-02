import buscarColaborador


class ADP:

    def __init__(self, empresa, usuario, senha, link='https://www.adpexpertbrasil.com'):
        self.__empresa = empresa
        self.__usuario = usuario
        self.__senha = senha
        self.__link = link


    def setLink(self, link):
        self.__link = link


    def getLink(self):
        return self.__link


    def getUsuario(self):
        return self.__usuario


    def getSenha(self):
        return self.__senha


    def getEmpresa(self):
        return self.__empresa


    def setEmpresa(self, empresa):
        self.__empresa = empresa


    def resetSenha(self):
        pass


    def buscarColaborador(self, nome='', email='', cpf=''):
        '''
        :param nome: nome do colaborador
        :param email: e-mail do colaborador
        :param cpf: cpf do colaborador
        :return: (boolean) Se conseguiu ou não localizar o colaborador
        para o reset de sua senha no sistema ADP
        '''
        if buscarColaborador.buscarPorNome():
            return True
        elif buscarColaborador.buscarPorCpf():
            return True
        else:
            return False
