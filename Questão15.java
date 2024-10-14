interface Animal {
    String emitirSom();
}

class Cachorro implements Animal {
    public String emitirSom() {
        return "Au Au!";
    }
}

class Gato implements Animal {
    public String emitirSom() {
        return "Miau!";
    }
}

public class Main {
    public static void fazerSom(Animal animal) {
        System.out.println(animal.emitirSom());
    }

    public static void main(String[] args) {
        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        fazerSom(cachorro); 
        fazerSom(gato);     
    }
}
