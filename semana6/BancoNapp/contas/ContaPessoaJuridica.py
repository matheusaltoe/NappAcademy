from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de pessoa jurídica.
    Limite padrão da conta: R$ 1500,00

    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe PessoaJuridica.
        Extrai do dicionário kwargs o nome da empresa correntista.
        """
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)