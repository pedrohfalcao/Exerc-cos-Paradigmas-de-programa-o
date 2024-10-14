class Carro:
    """Classe que representa um carro."""

    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self) -> str:
        return f"{self.ano} {self.marca} {self.modelo}"

# Instanciando três objetos da classe Carro
carros = [
    Carro("Toyota", "Corolla", 2020),
    Carro("Honda", "Civic", 2019),
    Carro("Ford", "Fiesta", 2021)
]

for carro in carros:
    print(carro)
