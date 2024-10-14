package main

import (
    "fmt"
    "math"
)


type Forma interface {
    Area() float64
}

type Retangulo struct {
    Largura, Altura float64
}


func (r Retangulo) Area() float64 {
    return r.Largura * r.Altura
}

type Circulo struct {
    Raio float64
}


func (c Circulo) Area() float64 {
    return math.Pi * c.Raio * c.Raio
}

func main() {
    formas := []Forma{Retangulo{5, 10}, Circulo{7}}
    for _, forma := range formas {
        fmt.Printf("Área: %.2f\n", forma.Area())
    }
}
