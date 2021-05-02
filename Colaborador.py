class Colaborador:

    def __init__(self, empresa, empresaUsuario, empresaSenha, nome=None, email=None, cpf=None):
        self.__empresa = empresa
        self.__empresaUsuario = empresaUsuario
        self.__empresaSenha = empresaSenha
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf


    def getUsuario(self):
        '''
        :return: (string) Usuário para o login no sistema ADP referênte a empresa do colaborador
        '''
        return self.__empresaUsuario


    def setUsuario(self, empresaUsuario):
        '''
        Especifica usuário para o login no sistema ADP referênte a empresa do colaborador.
        :param empresaUsuario: (string) empresa do Colaborador.
        :return: None
        '''
        self.__empresaUsuario = empresaUsuario


    def getSenha(self):
        '''
        :return: (string) Senha para o login no sistema ADP referênte a empresa do colaborador.
        '''
        return self.__empresaSenha


    def setSenha(self, empresaSenha):
        '''
        Especifica senha para o login no sistema ADP referênte a empresa do colaborador.
        :param empresaSenha: (string) Senha referente ao login no sistema ADP
        referênte a empresa do colaborador.
        :return: None
        '''
        self.__empresaSenha = empresaSenha


    def getEmpresa(self):
        return self.__empresaSenha


    def setEmpresa(self, empresaSenha):
        self.__empresaSenha = empresaSenha


    def getEmail(self):
        if self.__email != None:
            return self.__email
        else:
            return None


    def setEmail(self, email):
        self.__email = email


    def getNome(self, nome):
        if self.__nome != None:
            return self.__nome
        else:
            return None


    def setNome(self, nome):
        self.__nome = nome


    def getCpf(self, cpf):
        if self.__cpf != None:
            return self.__cpf
        else:
            return None


    def setCpf(self, cpf):
        self.__cpf = cpf

