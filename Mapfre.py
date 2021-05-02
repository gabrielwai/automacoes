from ADP import ADP


class Mapfre(ADP):

    def __init__(self, empresa, usuario, senha):
        super().__init__(empresa)
        self.__usuario = usuario
        self.__senha = senha


    def getUsuario(self):
        return self.__usuario

    def getSenha(self):
        return self.__senha


