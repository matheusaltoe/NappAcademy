from abc import ABC, abstractmethod
from produtos.classes.Caracteristicas import Caracteristicas

class Produto(ABC):
    def __init__(self, implementation):
        self.implementation = implementation
        if issubclass(type(implementation), Caracteristicas):
            return
        raise Exception('Deve ser informado uma subclasse de Caracteristicas')

    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")


class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")


class GuaranaAntartica(Produto):
    def operation(self):
        return (f"GuaranaAntartica tamanho:"
                f"{self.implementation.operation_implementation()}")