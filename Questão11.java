abstract class Funcionario {
    public abstract double calcularSalario();
}

class FuncionarioHorista extends Funcionario {
    private String nome;
    private double horasTrabalhadas;
    private double valorHora;

    public FuncionarioHorista(String nome, double horasTrabalhadas, double valorHora) {
        this.nome = nome;
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorHora = valorHora;
    }

    @Override
    public double calcularSalario() {
        return horasTrabalhadas * valorHora;
    }

    public String getNome() {
        return nome;
    }
}

class FuncionarioAssalariado extends Funcionario {
    private String nome;
    private double salario;

    public FuncionarioAssalariado(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }

    @Override
    public double calcularSalario() {
        return salario;
    }

    public String getNome() {
        return nome;
    }
}

public class Main {
    public static void main(String[] args) {
        Funcionario[] funcionarios = {
            new FuncionarioHorista("Alice", 160, 50),
            new FuncionarioAssalariado("Bob", 4000)
        };

        for (Funcionario f : funcionarios) {
            System.out.printf("Salário de %s: R$%.2f%n", f.getNome(), f.calcularSalario());
        }
    }
}
