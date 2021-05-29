from SistemaADP.ADP import ADP
from SistemaADP.Administrador import Administrador
from Colaborador import Colaborador
from Empresas import Empresas
from Chamados.Chamado import Chamado


adp = ADP()

colaborador1 = Colaborador(Empresas.BRASILSEG.name, nome='Someone')
adm1 = Administrador(colaborador1.getEmpresa())

adp.login(adm1, colaborador1.getEmpresa())
adp.resetSenha(colaborador1)


ch1 = Chamado.novoChamado('RF345245')
print(ch1.getCodigoChamado())
ch2 = Chamado.novoChamado("IM123456")
print(ch2.getCodigoChamado())
