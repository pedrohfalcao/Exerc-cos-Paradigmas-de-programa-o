package main

import "fmt"


type Carro struct {
    Marca     string
    Modelo    string
    Ano       int
    Velocidade int
}


func (c *Carro) Acelerar(incremento int) {
    c.Velocidade += incremento
}


func (c *Carro) Frear(decremento int) {
    if c.Velocidade-decremento < 0 {
        c.Velocidade = 0
    } else {
        c.Velocidade -= decremento
    }
}

func main() {
    carro := Carro{"Toyota", "Corolla", 2020, 0}
    carro.Acelerar(50)
    fmt.Printf("Velocidade: %d km/h\n", carro.Velocidade)
    carro.Frear(20)
    fmt.Printf("Velocidade: %d km/h\n", carro.Velocidade)
}
