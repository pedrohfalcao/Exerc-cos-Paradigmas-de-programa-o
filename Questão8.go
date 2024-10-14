package main

import "fmt"


type Empregado struct {
    Nome   string
    Cargo  string
    Salario float64
}


type Empresa struct {
    Nome      string
    Empregados []Empregado
}


func (e *Empresa) AdicionarEmpregado(emp Empregado) {
    e.Empregados = append(e.Empregados, emp)
}


func (e Empresa) ListarEmpregados() {
    fmt.Println("Empregados da empresa", e.Nome)
    for _, emp := range e.Empregados {
        fmt.Printf("%s - %s - R$%.2f\n", emp.Nome, emp.Cargo, emp.Salario)
    }
}

func main() {
    empresa := Empresa{Nome: "Tech Solutions"}
    emp1 := Empregado{"Alice", "Desenvolvedora", 8000.00}
    emp2 := Empregado{"Bob", "Gerente de Projetos", 12000.00}
    
    empresa.AdicionarEmpregado(emp1)
    empresa.AdicionarEmpregado(emp2)
    
    empresa.ListarEmpregados()
}
