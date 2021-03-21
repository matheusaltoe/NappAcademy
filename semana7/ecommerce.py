from ecommerce.classes.Pedido import Pedido
from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Ecommerce import Loja


loja = Loja('Loja Napp', saldo_caixa=3000)
loja.add_estoque('123', 15, 10)
loja.add_estoque('1234', 20, 5)
loja.add_estoque('999', 50, 2)

pedido = Pedido(Cliente('José da Silva'))
cliente = Cliente('John Doe')
pedido2 = Pedido(cliente)

pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))
pedido.add_item(loja.comprar('1234'))
pedido.add_item(loja.comprar('123'))

pedido2.add_item(loja.comprar('1234'))
pedido2.add_item(loja.comprar('123'))
pedido2.add_item(loja.comprar('999'))

loja.devolver_carrinho(pedido)
pedido2.checkout('dinheiro')
loja.soma_caixa(pedido2.valor_total_pagar())