class Animal:
    """Classe base que representa um animal."""

    def som(self) -> str:
        raise NotImplementedError("Subclasse deve implementar este método.")

class Cachorro(Animal):
    def som(self) -> str:
        return "Au Au"

class Gato(Animal):
    def som(self) -> str:
        return "Miau"


def emitir_som(animal: Animal) -> None:
    print(animal.som())

cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)  
emitir_som(gato)      
