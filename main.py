from NavegadorFactory import NavegadorFactory
from SistemaADP.ADP import ADP
from SistemaADP.Administrador import Administrador
from Colaborador import Colaborador
from Empresas import Empresas
from Chamados.ChamadoConcreteFactory import Chamado
from Chamados.Incidente import Incidente
from Chamados.HPServiceManager import HPServiceManager


navegador = NavegadorFactory.criarEdge(background=False)
adp = ADP(tipoNavegador=navegador)
