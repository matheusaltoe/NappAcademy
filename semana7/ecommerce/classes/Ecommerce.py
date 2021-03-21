from ecommerce.classes.Produto import Produto
from ecommerce.classes.Pedido import Pedido


class Loja:
    def __init__(self, nome, **kwargs):
        self._nome = nome
        self._estoque = []
        self._saldo_caixa = kwargs.get('saldo_caixa', 5000)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estoque(self):
        return self._estoque
    
    @property
    def saldo_caixa(self):
        return self._saldo_caixa
    
    @saldo_caixa.setter
    def saldo_caixa(self, value):
        self._saldo_caixa = value

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Nome da Loja => ' + self.nome

    def add_estoque(self, ean, preco, quantidade):
        for i in range(quantidade):
            self._estoque.append(Produto(ean=ean, preco=preco, quantidade=quantidade))

    def quantidade_produtos(self, ean):
        quantidade = 0
        for produto in self.estoque:
            if produto.ean == ean:
                quantidade = quantidade + 1
        return quantidade

    def comprar(self, ean):
        for produto in self.estoque:
            if str(produto) == ean:
                self._estoque.remove(produto)
                return produto
        return None

    def devolver_carrinho(self, pedido):
        if isinstance(pedido, Pedido):
            for item in pedido.itens:
                if isinstance(item, Produto):
                    self._estoque.append(item)
            pedido.itens = []
            return pedido

    def soma_caixa(self, total_venda):
        self.saldo_caixa += total_venda   
