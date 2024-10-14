class Motor:
    """Classe que representa um motor."""
    
    def __init__(self, potencia: int) -> None:
        self.potencia = potencia

class Carro:
    """Classe que representa um carro com motor."""
    
    def __init__(self, marca: str, modelo: str, motor: Motor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def detalhes(self) -> str:
        return f"{self.marca} {self.modelo} com motor de {self.motor.potencia} HP"


motor = Motor(150)
carro = Carro("Ford", "Mustang", motor)
print(carro.detalhes())  
