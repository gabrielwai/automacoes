from NavegadorFactory import NavegadorFactory
from SistemaADP.ADP import ADP
from SistemaADP.Administrador import Administrador
from Colaborador import Colaborador
from Empresas import Empresas
from Chamados.ChamadoConcreteFactory import Chamado
from Chamados.Incidente import Incidente
from Chamados.HPServiceManager import HPServiceManager
from Chrome import Chrome


navegador = NavegadorFactory.criarFireFox(background=False)
adp = ADP(tipoNavegador=navegador)
adp.getTesteNavegador()
exit()

print(Empresas.MAPFRE.name, type(Empresas.MAPFRE.name)); exit()
#adp = ADP(backgorund=False)
inc = Incidente('IM02241369')
hp = HPServiceManager()
if hp.login():
    inc.localizarChamado(hp)
exit()
colaborador1 = Colaborador("Brasilseg", nome='gabriel wAI')
adm1 = Administrador(colaborador1.getEmpresa())

adp.login(adm1, colaborador1.getEmpresa())
adp.resetSenha(colaborador1)


ch1 = Chamado.novoChamado('RF345245')
print(ch1.getCodigoChamado())
ch2 = Chamado.novoChamado("IM123456")
print(ch2.getCodigoChamado())
