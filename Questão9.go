package main

import "fmt"


type Autor struct {
    Nome string
}


type Livro struct {
    Titulo string
    Autor  Autor
}


func (l Livro) Detalhes() string {
    return fmt.Sprintf("%s escrito por %s", l.Titulo, l.Autor.Nome)
}

func main() {
    autor := Autor{Nome: "George Orwell"}
    livro := Livro{Titulo: "1984", Autor: autor}
    fmt.Println(livro.Detalhes()) 
}
