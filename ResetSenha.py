import buscarColaborador


def resetSenhaADP(chamadoID, usuario, senha, nomeColaborador=None, emailColaborador=None, cpfColaborador=None):
    if not buscarColaborador.buscarPorNome(usuario, senha, nomeColaborador):
        if not buscarColaborador.buscarPorCpf(usuario, senha, cpfColaborador):
            return False
        else:
            __resetSenha()
    else:
        __resetSenha()


def __resetSenha():
    pass
