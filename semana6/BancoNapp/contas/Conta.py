from BancoNapp.exception.erros import (
    DepositoMaiorZero,
    DepositoNumerico,
    SaqueNumerico,
    DepositoSuperaSaqueLimite,
    SaldoMenorZero,
    JurosEntreUmECem,
)

class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe por kwargs :
        - nome
        - limite
        - saldo
        - juros

        Raises:
            ValueError: Caso o saldo seja menor ou igual a zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.juros = kwargs.get('juros', 0.11)
        saldo = kwargs.get('saldo', 0)
        if saldo < 0:
            SaldoMenorZero()
        self.saldo = saldo
        self.extrato.append(('I', saldo))

    def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                DepositoMaiorZero()
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        DepositoNumerico()

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                DepositoSuperaSaqueLimite()
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        SaqueNumerico()

    def get_extrato(self):
        """
        Retorna a lista dos saques e depósitos feitos na conta.

        Returns:
            List: Lista de operações
        """
        return self.extrato

    def rendimento_aniversario(self, juros):
        """
        Retorna os valores de rendimento dos depósitos feitos na conta.

        Returns:
            Float: Rendimento dos juros
        """
        if juros < 0 or juros > 1:
            JurosEntreUmECem()
            return 
        total = self.saldo * juros
        self.saldo += total
        return total
