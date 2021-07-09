from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from Chamados.HPLoginErros import HPLoginErros
import time

# from selenium import webdriver
# #
# x = webdriver.Chrome()
# x.find_element_by_id('ext-gen-top5')
# x.window_handles()
# x.switch_to.frame()


def loginHPServiceManager(navegador, link, usuario, senha, statusLogin=True):

    login = str(usuario) + ":" + str(senha) + "@"
    url = link[:len('https://')] + login
    url = url + link[len('https://'):]
    navegador.get(url)
    try:
        navegador.implicitly_wait(30)
        navegador.find_element_by_xpath('//*[@id="ext-gen-top107"]').is_displayed()
    except NoSuchElementException:
        if statusLogin:
            __HPLoginFail(HPLoginErros.CredenciaisInvalidas.value)
        return False
    except AttributeError:
        if statusLogin:
            __HPLoginFail(HPLoginErros.AcessoNegado.name)
        return False
    # verifica se a página carregou completamente, com sucesso, só para depois retornar o login bem sucedido:
    contador = 0
    exceptions = 0
    while exceptions == contador:
        print('Start')
        try:
            navegador.find_element_by_xpath('//*[@id="ext-gen-top172"]').click()
        except ElementClickInterceptedException or NoSuchElementException:
            print('Deu ruim')
            exceptions += 1
            exceptions = exceptions % 2
            print(f'exceptions: {exceptions}')
        contador += 1
        contador = contador % 2
        print(f'contador: {contador}')
    print(f'sai; contador = {contador}')
    x = navegador.find_element_by_xpath('//*[@id="ext-gen-top172"]')
    print(x)
    x.click()
    print('retornando da função')
    return True


# def __HPloginStatus(excessao, statusLogin=False):
#     if statusLogin:
#         print('HP Service Manager - login status:')
#
#         excessoes = dict()
#         excessoes['Acesso Negado'] = "Acesso Negado, o número máximo de logons ativos para este usuário foi excedido.; tente novamente mais tarde."
#         excessoes['credenciais invalidas'] = "Verifique suas credenciais de acesso."
#
#         print(excessoes[excessao])


def __HPLoginFail(tipoErro):
    print('HP Service Manager - login status:')
    print(tipoErro)


def localizar(chamado, HPServiceManager_navegador, xpath):
    navegador = HPServiceManager_navegador
    navegador.implicitly_wait(35)
    # WebDriverWait(navegador, 35).until(EC.element_to_be_selected((By.XPATH, xpath)))
    navegador.find_element_by_xpath(xpath).click()
    navegador.find_element_by_xpath('//*[@id="ext-gen-top186"]').click()
    print("Clicou")

    a = '//*[@id="X11"]'
    navegador.implicitly_wait(35)
    navegador.switch_to.frame(navegador.find_element(By.CSS_SELECTOR, "iframe[title='Exibir quais Registros de Incidente?']"))
    navegador.find_element_by_xpath(a).send_keys(chamado)
    navegador.find_element_by_xpath(a).send_keys(Keys.RETURN)
    print('Tentei já...')
    return True
    #print("handles", navegador.window_handles())
    #navegador.switch_to.frame('mif-comp-ext-gen-top66-355310')
    print(f'Existem {len(frames)} frames na página. {frames}')
    for element in frames:
        print(f'id : {element.get_attribute("id")}; frame name: {element.get_attribute("name")}; frame css_selector: {element.get_attribute("css_selector")}')
        try:
            navegador.switch_to.frame(element.get_attribute("name"))
            print(f'mudou para frame: {element.get_attribute("name")}')
            navegador.find_element_by_xpath(a)
        except:
            #print(f'frame {element.get_attribute("name")} falhou.')
            print('Nada')
    #navegador.switch_to.frame('downloadiframe')
        print('---------------')
        #print(f'DEU BOM! : {element}; {element.get_attribute("name")}')
    contador = 0
    exceptions = 0
    while exceptions == contador:
        print('Start 2')
        iframeID = 'mif-comp-ext-gen-top313-615233'
        #iframeID = 'mif-comp-ext-gen-top313-615233'
        #iframeID = 'ext-comp-917816'
        #iframeID = 'mif-comp-ext-gen-top313-30031'
        #iframeID = 'mif-comp-ext-gen-top313-864333'
        #navegador.switch_to.frame(iframeID)
        element = navegador.find_element_by_xpath(a)
        print(element, element.is_selected(), element.is_displayed())
        try:
            # element = navegador.find_element_by_xpath(a)
            # print(element, element.is_selected(), element.is_displayed())
            element.click()
        except NoSuchElementException:
            print('Deu ruim 2')
            exceptions += 1
            exceptions = exceptions % 2
            print(exceptions)
        contador += 1
        contador = contador % 2
    print(f'Saldo - contador: {contador}')

    #print(f'X11 is selected? = {navegador.find_element_by_xpath(a).is_selected()}')
    navegador.find_element_by_xpath(a).click()
    navegador.find_element_by_xpath(a).send_keys(chamado + Keys.ENTER)
    print('GG')

    #navegador.find_element_by_id('ext-gen-top186').click()
    # navegador.find_element_by_id('X11').send_keys(chamado + Keys.ENTER)
    # navegador.find_element_by_xpath("//input[@type='text']").send_keys(chamado + Keys.ENTER)
    #WebDriverWait(navegador, 30).until(EC.element_to_be_clickable('X11'))
    # print('FOI!')
    # navegador.implicitly_wait(35)

def atualizar(navegador, chamado):
    pass


def resolver():
    pass