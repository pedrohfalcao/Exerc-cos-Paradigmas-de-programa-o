class Autor {
    private String nome;

    public Autor(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }
}

class Livro {
    private String titulo;
    private Autor autor;

    public Livro(String titulo, Autor autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    public String detalhes() {
        return titulo + " escrito por " + autor.getNome();
    }

    public static void main(String[] args) {
        Autor autor = new Autor("George Orwell");
        Livro livro = new Livro("1984", autor);
        System.out.println(livro.detalhes()); 
    }
}
