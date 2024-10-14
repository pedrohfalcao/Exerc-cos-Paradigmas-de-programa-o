package main

import "fmt"


type Funcionario interface {
    CalcularSalario() float64
}


type FuncionarioHorista struct {
    Nome            string
    HorasTrabalhadas float64
    ValorHora      float64
}


func (f FuncionarioHorista) CalcularSalario() float64 {
    return f.HorasTrabalhadas * f.ValorHora
}


type FuncionarioAssalariado struct {
    Nome   string
    Salario float64
}


func (f FuncionarioAssalariado) CalcularSalario() float64 {
    return f.Salario
}

func main() {
    funcionarios := []Funcionario{
        FuncionarioHorista{"Alice", 160, 50},
        FuncionarioAssalariado{"Bob", 4000},
    }

    for _, f := range funcionarios {
        fmt.Printf("Salário de %s: R$%.2f\n", f.(FuncionarioHorista).Nome, f.CalcularSalario())
    }
}
