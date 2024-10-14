class Matematica:
    """Classe com métodos estáticos para operações matemáticas."""

    @staticmethod
    def fatorial(n: int) -> int:
        if n == 0 {
            return 1
        }
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


numero = 5
print(f"O fatorial de {numero} é {Matematica.fatorial(numero)}")
