import java.util.ArrayList;
import java.util.List;

class Escola {
    private String nome;
    private List<Professor> professores;

    public Escola(String nome) {
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    public void adicionarProfessor(Professor professor) {
        professores.add(professor);
    }

    public String getNome() {
        return nome;
    }

    public List<Professor> getProfessores() {
        return professores;
    }
}

class Professor {
    private String nome;

    public Professor(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }
}

public class Main {
    public static void main(String[] args) {
        Escola escola = new Escola("Escola Primária");
        Professor prof1 = new Professor("Alice");
        Professor prof2 = new Professor("Bob");
        
        escola.adicionarProfessor(prof1);
        escola.adicionarProfessor(prof2);
        
        System.out.println("Professores da " + escola.getNome() + ":");
        for (Professor professor : escola.getProfessores()) {
            System.out.println(professor.getNome());
        }
    }
}
