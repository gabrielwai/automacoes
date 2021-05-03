def registrarChamado(chamadoID, descricao):
    # Registrar chamado:
    with open("registros/chamados-completados.txt", 'a') as f:
        f.write(chamadoID + '\n')
    # registrar descrição:
    with open("registros/chamados-descricao.txt", 'a') as f:
        f.write(descricao + '\n')


def registrarFalha(chamadoID):
    '''Registrar chamado que não se foi possível resolver
    por não ter conseguido encontrar o colaborador'''
    with open("registros/chamados-N-resolvidos.txt", 'a') as f:
        f.write(chamadoID + '\n')
