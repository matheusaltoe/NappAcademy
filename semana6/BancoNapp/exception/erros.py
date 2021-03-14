class DepositoMaiorZero(Exception):
    def __init__(self):
        raise ValueError('Valor do depósito precisa ser maior que zero')

class DepositoNumerico(Exception):
    def __init__(self):
        raise TypeError('O depósito precisa ser numérico')

class SaqueNumerico(Exception):
    def __init__(self):
        raise TypeError('O valor do saque precisa ser numérico')        

class DepositoSuperaSaqueLimite(Exception):
    def __init__(self):
        raise ValueError('Valor do saque supera seu saldo e seu limite')

class DepositoSuperaSaque(Exception):
    def __init__(self):
        raise ValueError('Valor do saque supera seu saldo.')        

class SaldoMenorZero(Exception):
    def __init__(self):
        raise ValueError('Saldo negativo')

class JurosEntreUmECem(Exception):
    def __init__(self):
        raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
