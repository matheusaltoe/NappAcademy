from BancoNapp.contas.Conta import Conta
from BancoNapp.exception.erros import DepositoSuperaSaqueLimite, DepositoSuperaSaque, SaqueNumerico


class ContaPoupanca(Conta):
    """
    Classe representa a conta poupança.

    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        self.profissao = kwargs.get('profissao', '')
        """
        Construtor da classe ContaPoupança.
        """
        super(ContaPoupanca, self).__init__(**kwargs)
        self.nome = kwargs.get('nome')
        self.limite = kwargs.get('limite', 0)

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
            if valor > self.saldo:
                DepositoSuperaSaque()
                return
            if valor > (self.saldo + self.limite):
                DepositoSuperaSaqueLimite()
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        SaqueNumerico()
        return super().saque()          
