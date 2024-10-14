abstract class Animal {
    public abstract String som();
}

class Cachorro extends Animal {
    @Override
    public String som() {
        return "Au Au";
    }
}

class Gato extends Animal {
    @Override
    public String som() {
        return "Miau";
    }
}

public class Main {
    public static void main(String[] args) {
        Animal[] animais = { new Cachorro(), new Gato() };
        emitirSons(animais);
    }

    public static void emitirSons(Animal[] animais) {
        for (Animal animal : animais) {
            System.out.println(animal.som());
        }
    }
}
