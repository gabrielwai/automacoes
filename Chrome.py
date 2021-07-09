from Navegador import Navegador
from selenium import webdriver


class Chrome(Navegador):

    def criarNavegador(self):
        self._navegador = webdriver.Chrome(options=self._getOptions())
        self._getNavegador()

