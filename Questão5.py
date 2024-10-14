class Animal:
    def som(self):
        raise NotImplementedError("Subclasse deve implementar este método.")

class Cachorro(Animal):
    def som(self):
        return "Au Au"

class Gato(Animal):
    def som(self):
        return "Miau"

def emitir_som(animais):
    for animal in animais:
        print(animal.som())

animais = [Cachorro(), Gato()]
emitir_som(animais)  
