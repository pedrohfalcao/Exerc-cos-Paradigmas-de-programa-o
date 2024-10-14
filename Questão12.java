class Produto {
    private String nome;
    private double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public Produto combinar(Produto outro) {
        return new Produto(this.nome + " e " + outro.nome, this.preco + outro.preco);
    }
}

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Camiseta", 50.00);
        Produto produto2 = new Produto("Calça", 100.00);
        Produto produtoCombinado = produto1.combinar(produto2);
        System.out.printf("Produto combinado: %s - R$%.2f%n", produtoCombinado.getNome(), produtoCombinado.getPreco());
    }
}
