class Colaborador:

    def __init__(self, empresa, empresaUsuario, empresaSenha, email=None):
        self.__empresa = empresa
        self.__empresaUsuario = empresaUsuario
        self.__empresaSenha = empresaSenha
        self.__email = email


    def getUsuario(self):
        return self.__empresaUsuario


    def setUsuario(self, empresaUsuario):
        self.__empresaUsuario = empresaUsuario


    def getSenha(self):
        return self.__empresaSenha


    def setSenha(self, empresaSenha):
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
        return self.__nome


    def setNome(self, nome):
        self.__nome = nome


    def getCpf(self, cpf):
        return self.__cpf


    def setCpf(self, cpf):
        self.__cpf = cpf

