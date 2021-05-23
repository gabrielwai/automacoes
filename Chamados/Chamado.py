class Chamado():

    def __init__(self, SD=None):
        self.__chamados = set()
        self.__SD = SD


    def getSD(self):
        return self.__SD


    def setSD(self, SD):
        self.__SD = SD


    def adicionarChamadoRelacionado(self, chamado):
        self.__chamados.add(chamado.strip().upper())


    def getChamadosRelacionados(self):
        return self.__chamados


    def removerChamadoRelacionado(self, chamado):
        chamado = chamado.strip().upper()
        # if chamado not in self.__chamados:
        #     print(f"Chamado '{chamado}' não está relacionado com '{self.getSD()}'")
        self.__chamados.discard(chamado)
