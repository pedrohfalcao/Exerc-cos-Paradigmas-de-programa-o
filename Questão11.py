from abc import ABC, abstractmethod

class Funcionario(ABC):
    """Classe abstrata que representa um funcionário."""

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class FuncionarioHorista(Funcionario):
    """Classe que representa um funcionário horista."""
    
    def __init__(self, nome: str, horas_trabalhadas: float, valor_hora: float) -> None:
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> float:
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioAssalariado(Funcionario):
    """Classe que representa um funcionário assalariado."""
    
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def calcular_salario(self) -> float:
        return self.salario


funcionarios = [
    FuncionarioHorista("Alice", 160, 50),
    FuncionarioAssalariado("Bob", 4000)
]

for funcionario in funcionarios:
    print(f"Salário de {funcionario.nome}: R${funcionario.calcular_salario():.2f}")
