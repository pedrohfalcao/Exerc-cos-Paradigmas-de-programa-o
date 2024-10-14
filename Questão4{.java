abstract class Animal {
    public abstract String som(); 
}

class Cachorro extends Animal {
    @Override
    public String som() {
        return "Au Au";
    }
}

class Gato extends
@Override
    public String som() {
        return "Miau";
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();
        
        emitirSom(cachorro); 
        emitirSom(gato);     
    }

    public static void emitirSom(Animal animal) {
        System.out.println(animal.som());
    }
}