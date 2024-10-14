class Carro:
    """Classe que representa um carro."""

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento: int) -> None:
        self.velocidade += incremento

    def frear(self, decremento: int) -> None:
        self.velocidade = max(0, self.velocidade - decremento)

    def get_velocidade(self) -> int:
        return self.velocidade


carro = Carro("Toyota", "Corolla", 2020)
carro.acelerar(50)
print(f"Velocidade: {carro.get_velocidade()} km/h")
carro.frear(20)
print(f"Velocidade: {carro.get_velocidade()} km/h")
