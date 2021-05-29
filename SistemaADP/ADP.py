from Empresas import Empresas
from selenium import webdriver
import Automacoes.ADP


class ADP:
#futuras classes filhas da ADP: menu_full; painel_1 (interface); adm_seg
    def __init__(self, link='https://expert.brasil.adp.com/', background=True):
        self.__navegador = None
        self.__link = link
        self.__background = background


    def __setup(self):
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1280,720")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.__navegador = webdriver.Chrome(options=self.options)


    def login(self, administrador, empresa):
        if self.__background:
           self.__setup()
        else:
            self.__navegador = webdriver.Chrome()

        verificador = True

        if not (bool(administrador.getUsuario()) and bool(administrador.getSenha())):
            print('Insira o login para acesso ao sistema ADP no arquivo xml destinado ao administrador.')
            print('Falha ao realizar o login no sistema ADP.'); exit()

        empresa = empresa.strip().upper()
        for emp in Empresas:
            if emp.name in empresa:
                if Automacoes.ADP.login(self.__getNavegador(), self.__link, administrador.getUsuario(), administrador.getSenha()):
                    Automacoes.ADP.escolherEmpresa(self.__getNavegador(), emp.name)
                    verificador = False
        if verificador:
            print("Erro ao efetuar o login, verifique suas credenciais.")
            exit()
            return False
        else:
            return True


    def getLink(self):
        return self.__link


    def __getNavegador(self):
        return self.__navegador


    def resetSenha(self, colaborador):
        if Automacoes.ADP.buscarColaborador(self.__getNavegador(), colaborador):
            Automacoes.ADP.resetarSenha(self.__getNavegador(), colaborador)
            return True
        else:
            print("Usuário não encontrado para reset de senha:",
                  colaborador.getNome(), colaborador.getEmail(), colaborador.getCpf(),
                  "- empresa:", colaborador.getEmpresa())
            return False
