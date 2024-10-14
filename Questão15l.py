from typing import Protocol

class Animal(Protocol):
    """Interface que define métodos para um animal."""
    
    def emitir_som(self) -> str:
        pass

class Cachorro:
    """Classe que representa um cachorro."""
    
    def emitir_som(self) -> str:
        return "Au Au!"

class Gato:
    """Classe que representa um gato."""
    
    def emitir_som(self) -> str:
        return "Miau!"


def fazer_som(animal: Animal) -> None:
    print(animal.emitir_som())

cachorro = Cachorro()
gato = Gato()

fazer_som(cachorro)  
fazer_som(gato)      
