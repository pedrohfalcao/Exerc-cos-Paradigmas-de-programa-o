class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private int velocidade;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }

    public void acelerar(int incremento) {
        velocidade += incremento;
    }

    public void frear(int decremento) {
        velocidade = Math.max(0, velocidade - decremento);
    }

    public int getVelocidade() {
        return velocidade;
    }

    public static void main(String[] args) {
        Carro carro = new Carro("Toyota", "Corolla", 2020);
        carro.acelerar(50);
        System.out.println("Velocidade: " + carro.getVelocidade() + " km/h");
        carro.frear(20);
        System.out.println("Velocidade: " + carro.getVelocidade() + " km/h");
    }
}
