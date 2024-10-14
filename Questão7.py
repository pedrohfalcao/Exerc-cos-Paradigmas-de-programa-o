class Escola:
    """Classe que representa uma escola."""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor) -> None:
        self.professores.append(professor)

class Professor:
    """Classe que representa um professor."""

    def __init__(self, nome: str) -> None:
        self.nome = nome


escola = Escola("Escola Primária")
prof1 = Professor("Alice")
prof2 = Professor("Bob")
escola.adicionar_professor(prof1)
escola.adicionar_professor(prof2)

print(f"Professores da {escola.nome}: {[prof.nome for prof in escola.professores]}")
