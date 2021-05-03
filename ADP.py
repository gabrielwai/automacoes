import ResetSenha
import buscarColaborador
import Requisicao
import Incidente
from ResetSenha import resetSenhaADP
from Colaborador import Colaborador
from timesheets import registrarChamado
from timesheets import registrarFalha


class ADP:

    def __init__(self, Colaborador, link='https://www.adpexpertbrasil.com'):
        self.__link = link
        self.__colaborador = Colaborador

    def setLink(self, link):
        self.__link = link


    def getLink(self):
        return self.__link


    def getUsuario(self):
        '''
        :return: (string) Usuário para o login no sistema ADP referênte a empresa do colaborador.
        '''
        return self.__colaborador.getUsuario()


    def getSenha(self):
        '''
        :return: (string) Senha para o login no sistema ADP referênte a empresa do colaborador.
        '''
        return self.__colaborador.getSenha()


    def resetSenha(self, chamadoID):
        '''
        Método que efetivamente reseta a senha do colaborador para o sistema ADP
        :param chamadoID: ID do chamado
        :return: (boolean) Se conseguiu, ou não, resetar a senha
        '''
        if resetSenhaADP(chamadoID, self.__colaborador.getUsuario(), self.__colaborador.getSenha(),
                      self.__colaborador.getNome(), self.__colaborador.getEmail(),
                      self.__colaborador.getCpf(), self.getLink()):
            if chamadoID[0] == 'R':
                Requisicao.analisarChamado(chamadoID)
                Requisicao.resolverChamado(chamadoID)

                registrarChamado(chamadoID, self.getDescricao())
                return True
            else:
                Incidente.analisarChamado(chamadoID)
                Incidente.resolverChamado(chamadoID)

                registrarChamado(chamadoID, self.getDescricao())
                return True
        else:
            registrarFalha(chamadoID)
            return False


    def getDescricao(self):
        with open("config/descricao-padrao.txt", "r") as descricao:
            descricao.read()
        return descricao


    def buscarColaborador(self, nome=None, email=None, cpf=None):
        '''
        :param nome: nome do colaborador
        :param email: e-mail do colaborador
        :param cpf: cpf do colaborador
        :return: (boolean) Se conseguiu ou não localizar o colaborador
        para o reset de sua senha no sistema ADP
        '''
        if buscarColaborador.buscarPorNome():
            return True
        elif buscarColaborador.buscarPorCpf():
            return True
        else:
            return False


    def localizarColaborador(self, nome):
        # localizar colaborador pela 'Manutenção de Currículo' (menu_full)
        pass
