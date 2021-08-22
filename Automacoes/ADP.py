from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def login(navegador, link, usuario, senha):
    #navegador.maximize_window()
    navegador.get(link)
    navegador.find_element_by_xpath('//*[@id="login"]').send_keys(usuario)
    navegador.find_element_by_xpath('//*[@id="login-pw"]').send_keys(senha)
    navegador.find_element_by_xpath('/html/body/div/div/section[1]/div/form/div[3]/div/button').click()
    navegador.implicitly_wait(30)
    try:
        navegador.find_element_by_xpath('//*[@id="downshift-0-input"]').is_displayed()
    except NoSuchElementException:
        return False
    return True


def escolherEmpresa(navegador, empresa):
    # navegador.implicitly_wait(10)
    navegador.find_element_by_xpath('//*[@id="downshift-0-input"]').click()
    navegador.implicitly_wait(5)
    navegador.find_element_by_xpath('//*[@id="downshift-0-input"]').send_keys(empresa + Keys.ARROW_DOWN + Keys.RETURN)


def buscarColaborador(navegador, colaborador):
    navegador.implicitly_wait(10)

    if colaborador.is_terceiro():
        navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div[1]/nav/a[2]').click()

    navegador.find_element_by_name('name').send_keys(colaborador.getNome())
    navegador.find_element_by_name('email').send_keys(colaborador.getEmail())
    # Adicionando zeros a esquerda ao CPF se necessário:
    cpf = bool(int(colaborador.getCpf())) * colaborador.getCpf() + int(not bool(int(colaborador.getCpf()))) * ''
    navegador.find_element_by_name('documentId').send_keys(cpf)
    navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div/div[2]/form/div/div[4]/div/button[2]').click()
    navegador.implicitly_wait(15)
    try:
        navegador.find_element_by_xpath("//span[text()=';(']").is_displayed()
    except NoSuchElementException:
        return True
    return False


def resetarSenha(navegador, is_terceiro: bool):
    try:
        # verifica se há o retorno de mais de um usuário na busca do sistema
        navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div/div[3]/div/div[2]').is_displayed()
    except NoSuchElementException:
        # se houver o retorno de apenas um usuário:
        if is_terceiro:
            navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div[2]/div[3]/div/div/div/div[4]/button').click()
            navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[2]/div/button').click()
        else:
            navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div/div[3]/div/div/div/div[4]/button').click()
            navegador.find_element_by_xpath('//*[@id="js-react-app"]/div/div/div[4]/div[2]/div[3]/div/div/div[3]/div/div/div[2]/div/button').click()
        time.sleep(5)
        navegador.get_screenshot_as_file('screenshot-reset_senha.png')
        return True
    navegador.get_screenshot_as_file('screenshot-multiplos_usuarios.png')
    return False
