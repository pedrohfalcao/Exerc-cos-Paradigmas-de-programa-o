package main

import "fmt"


type Escola struct {
    Nome       string
    Professores []Professor
}


func (e *Escola) AdicionarProfessor(p Professor) {
    e.Professores = append(e.Professores, p)
}


type Professor struct {
    Nome string
}

func main() {
    escola := Escola{Nome: "Escola Primária"}
    prof1 := Professor{Nome: "Alice"}
    prof2 := Professor{Nome: "Bob"}
    
    escola.AdicionarProfessor(prof1)
    escola.AdicionarProfessor(prof2)
    
    fmt.Println("Professores da", escola.Nome)
    for _, professor := range escola.Professores {
        fmt.Println(professor.Nome)
    }
}
