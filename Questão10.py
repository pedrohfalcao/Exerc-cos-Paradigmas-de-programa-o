from abc import ABC, abstractmethod

class Forma(ABC):
    """Classe abstrata para formas geométricas."""

    @abstractmethod
    def area(self) -> float:
        pass

class Retangulo(Forma):
    """Classe que representa um retângulo."""
    
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura

class Circulo(Forma):
    """Classe que representa um círculo."""
    
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def area(self) -> float:
        return 3.14 * (self.raio ** 2)


formas = [Retangulo(5, 10), Circulo(7)]
for forma in formas:
    print(f"Área: {forma.area()}")
v