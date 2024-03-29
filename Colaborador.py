class Colaborador:

    def __init__(self, empresa: str, is_terceiro: bool, nome='', email='', cpf=''):

        self.__cpf = (11 - len(str(cpf))) * "0" + str(cpf)

        self.__empresa = empresa.strip().upper()

        self.__nome = nome.strip().upper()

        self.__email = email.strip().upper()

        self.__terceiro = bool(is_terceiro)


    def getEmpresa(self) -> str:
        return self.__empresa


    def is_terceiro(self) -> bool:
        return self.__terceiro


    def setEmpresa(self, empresa):
        self.__empresa = empresa.strip().upper()


    def getEmail(self):
        return self.__email


    def setEmail(self, email):
        self.__email = email.strip().upper()


    def getNome(self):
        return self.__nome


    def setNome(self, nome):
        self.__nome = nome.strip().upper()


    def getCpf(self):
        return self.__cpf


    def setCpf(self, cpf):
        self.__cpf = str(cpf).strip()
