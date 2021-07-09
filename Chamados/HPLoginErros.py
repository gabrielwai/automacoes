from enum import Enum


class HPLoginErros(Enum):
    AcessoNegado = "Acesso Negado, o número máximo de logons ativos para este usuário foi excedido; tente novamente mais tarde."
    CredenciaisInvalidas = "Verifique suas credenciais de acesso."
