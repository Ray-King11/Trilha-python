from abc import ABC, abstractmethod

class Forma(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

r = Retangulo(5, 6)
print(r.area)  # Saída: 30

