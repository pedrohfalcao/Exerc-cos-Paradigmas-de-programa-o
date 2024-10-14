class Empregado:
    """Classe que representa um empregado."""
    
    def __init__(self, nome: str, cargo: str, salario: float) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    """Classe que representa uma empresa."""
    
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.empregados = []

      def adicionar_empregado(self, empregado: Empregado) -> None:
        self.empregados.append(empregado)

    def listar_empregados(self) -> None:
        print(f"Empregados da empresa {self.nome}:")
        for emp in self.empregados:
            print(f"{emp.nome} - {emp.cargo} - R${emp.salario:.2f}")


empresa = Empresa("Tech Solutions")
emp1 = Empregado("Alice", "Desenvolvedora", 8000.00)
emp2 = Empregado("Bob", "Gerente de Projetos", 12000.00)

empresa.adicionar_empregado(emp1)
empresa.adicionar_empregado(emp2)

empresa.listar_empregados()

