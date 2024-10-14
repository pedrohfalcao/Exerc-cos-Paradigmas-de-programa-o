package main

import "fmt"

// Carro representa um carro.
type Carro struct {
    Marca  string
    Modelo string
    Ano    int
}

// Método para imprimir as informações do carro.
func (c Carro) String() string {
    return fmt.Sprintf("%d %s %s", c.Ano, c.Marca, c.Modelo)
}

func main() {
    carros := []Carro{
        {"Toyota", "Corolla", 2020},
        {"Honda", "Civic", 2019},
        {"Ford", "Fiesta", 2021},
    }

    for _, carro := range carros {
        fmt.Println(carro)
    }
}
