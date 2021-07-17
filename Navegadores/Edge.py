from Navegador import Navegador
from selenium import webdriver


class Edge(Navegador):

    def criarNavegador(self):
        self._navegador = webdriver.Edge(executable_path='./.interpretador/automacoes/Scripts/msedgedriver.exe')
        return self._navegador
