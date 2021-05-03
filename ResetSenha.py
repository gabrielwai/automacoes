import buscarColaborador
import selenium


def resetSenhaADP(chamadoID, usuario, senha, link, nomeColaborador=None, emailColaborador=None, cpfColaborador=None):
    if not buscarColaborador.buscarPorNome(usuario, senha, nomeColaborador, link):
        if not buscarColaborador.buscarPorCpf(usuario, senha, cpfColaborador, link):
            return False
        else:
            __resetSenha()
            return True
    else:
        __resetSenha()
        return True


def __resetSenha():
    pass
