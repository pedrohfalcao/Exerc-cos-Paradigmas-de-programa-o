class Produto:
    """Classe que representa um produto com um preço."""

    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __add__(self, outro: 'Produto') -> 'Produto':
        return Produto(f"{self.nome} e {outro.nome}", self.preco + outro.preco)


produto1 = Produto("Camiseta", 50.00)
produto2 = Produto("Calça", 100.00)
produto_combinado = produto1 + produto2
print(f"Produto combinado: {produto_combinado.nome} - R${produto_combinado.preco:.2f}")
