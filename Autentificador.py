class Autentificador:


    def __init__(self, usuario, senha):
        self.__autentificar(usuario, senha)


    def __autentificar(self, usuario, senha):
        return bool(usuario) and bool(senha)
