import java.util.ArrayList;
import java.util.List;

class Empregado {
    private String nome;
    private String cargo;
    private double salario;

    public Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public String getCargo() {
        return cargo;
    }

    public double getSalario() {
        return salario;
    }
}

class Empresa {
    private String nome;
    private List<Empregado> empregados;

    public Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    public void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    public void listarEmpregados() {
        System.out.println("Empregados da empresa " + nome + ":");
        for (Empregado emp : empregados) {
            System.out.println(emp.getNome() + " - " + emp.getCargo() + " - R$" + emp.getSalario());
        }
    }

    public static void main(String[] args) {
        Empresa empresa = new Empresa("Tech Solutions");
        Empregado emp1 = new Empregado("Alice", "Desenvolvedora", 8000.00);
        Empregado emp2 = new Empregado("Bob", "Gerente de Projetos", 12000.00);
        
        empresa.adicionarEmpregado(emp1);
        empresa.adicionarEmpregado(emp2);
        
        empresa.listarEmpregados();
    }
}
