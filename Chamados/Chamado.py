from Chamados.ChamadoFactory import ChamadoFactory
from Chamados.Interacao import Interacao
from Chamados.Incidente import Incidente
from Chamados.Requisicao import Requisicao


class Chamado(ChamadoFactory):


    @classmethod
    def novoChamado(cls, codigoChamado):
        tipo = codigoChamado[:2]

        if tipo == 'SD':
            return Interacao()
        elif tipo == 'IM':
            return Incidente(codigoChamado)
        elif tipo == 'RF':
            return Requisicao(codigoChamado)
        else:
            return None
