abstract class Forma {
    public abstract double area();
}

class Retangulo extends Forma {
    private double largura;
    private double altura;

    public Retangulo(double largura, double altura) {
        this.largura = largura;
        this.altura = altura;
    }

    @Override
    public double area() {
        return largura * altura;
    }
}

class Circulo extends Forma {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    @Override
    public double area() {
        return Math.PI * raio * raio;
    }
}

public class Main {
    public static void main(String[] args) {
        Forma[] formas = { new Retangulo(5, 10), new Circulo(7) };
        for (Forma forma : formas) {
            System.out.println("Área: " + forma.area());
        }
    }
}
