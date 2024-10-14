class Carro {
    private String marca;
    private String modelo;
    private int ano;

    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    @Override
    public String toString() {
        return ano + " " + marca + " " + modelo;
    }

    public static void main(String[] args) {
        Carro[] carros = {
            new Carro("Toyota", "Corolla", 2020),
            new Carro("Honda", "Civic", 2019),
            new Carro("Ford", "Fiesta", 2021)
        };

        for (Carro carro : carros) {
            System.out.println(carro);
        }
    }
}
