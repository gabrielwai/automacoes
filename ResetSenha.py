import buscarColaborador


def resetSenhaADP(chamadoID, usuario, senha, link, nomeColaborador=None, emailColaborador=None, cpfColaborador=None):
    if not buscarColaborador.buscarPorNome(usuario, senha, nomeColaborador, link):
        if not buscarColaborador.buscarPorCpf(usuario, senha, cpfColaborador, link):
            return False
        else:
            __resetSenha()
    else:
        __resetSenha()


def __resetSenha():
    pass
