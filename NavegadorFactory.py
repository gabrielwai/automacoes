from Navegadores.Chrome import Chrome
from Navegadores.FireFox import FireFox
from Navegadores.Edge import Edge
from NavegadorAbstractFactory import NavegadorAbstractFactory
from selenium import webdriver


class NavegadorFactory(NavegadorAbstractFactory):

    # @classmethod
    # def criarNavegador(cls, backgorund=True):
    #     options = None
    #
    #     if backgorund:
    #         options = cls.__setup()
    #
    #     navegador = Navegador(options=options)
    #     return navegador.getNavegador()


    @classmethod
    def criarFireFox(cls, background=True):
        options = None

        if background:
            options = cls.__setup()

        navegador = FireFox()
        navegador.setOptions(options)
        return navegador


    @classmethod
    def criarChrome(cls, background=True):
        options = None

        if background:
            options = cls.__setup()

        navegador = Chrome()
        navegador.setOptions(options)
        return navegador


    @classmethod
    def criarEdge(cls, background=True):
        options = None

        if background & 0: # Microsoft Edge ainda não possui a funcionalidade de rodar em background na aplicação.
            options = cls.__setup()

        navegador = Edge()
        navegador.setOptions(options)
        return navegador


    @staticmethod
    def __setup():
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 " \
                     "(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1280,720")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        return options
