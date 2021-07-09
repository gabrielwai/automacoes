from Navegador import Navegador
from selenium import webdriver


class FireFox(Navegador):

    def criarNavegador(self):
        self._navegador = webdriver.Firefox(options=self._getOptions())
        self._getNavegador()

