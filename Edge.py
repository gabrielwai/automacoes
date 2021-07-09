from Navegador import Navegador
from selenium import webdriver


class Edge(Navegador):

    def criarNavegador(self):
        self._navegador = webdriver.Edge(options=self._getOptions())
        self._getNavegador()
