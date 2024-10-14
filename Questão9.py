class Autor:
    """Classe que representa um autor."""
    
    def __init__(self, nome: str) -> None:
        self.nome = nome

class Livro:
    """Classe que representa um livro com um autor."""
    
    def __init__(self, titulo: str, autor: Autor) -> None:
        self.titulo = titulo
        self.autor = autor

    def detalhes(self) -> str:
        return f"{self.titulo} escrito por {self.autor.nome}"


autor = Autor("George Orwell")
livro = Livro("1984", autor)
print(livro.detalhes())  