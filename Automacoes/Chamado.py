from selenium.webdriver.common.keys import Keys


def loginHPServiceManager(navegador, link, usuario, senha):

    login = str(usuario) + ":" + str(senha) + "@"
    url = link[:len('https://')] + login
    url = url + link[len('https://'):]
    navegador.get(url)
    try:
        navegador.find_element_by_xpath('//*[@id="ext-gen-top107"]').is_displayed()
    except:
        return False
    return True


def atualizarChamado(navegador, chamado):
    pass


def resolverChamado():
    pass