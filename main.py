from NavegadorFactory import NavegadorFactory
from SistemaADP.ADP import ADP
from Colaborador import Colaborador
from Chamados.Incidente import Incidente
from Chamados.HPServiceManager import HPServiceManager
from time import sleep


def main() -> None:
    '''
    adp = ADP(tipoNavegador=NavegadorFactory.criarChrome(background=True))
    colaborador1 = Colaborador("BRASILSEG", is_terceiro=True, nome="Gabriel Wai")
    
    adp.login('Joao.Silva.25', 'Adp@123BSG', 'BRASILSEG')
    adp.resetSenha(colaborador1)
    '''
    navegador2 = NavegadorFactory.criarChrome(background=False)
    hp = HPServiceManager("JVDSILVA", "Mapfre2021$!", navegador2)
    
    IM = Incidente("IM02523288")
    IM.localizarChamado(hp)
    
    sleep(225)


if __name__ == '__main__':
    main()