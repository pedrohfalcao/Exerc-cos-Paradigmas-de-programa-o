package main

import "fmt"


type Motor struct {
    Potencia int
}


type Carro struct {
    Marca  string
    Modelo string
    Motor  Motor
}


func (c Carro) Detalhes() string {
    return fmt.Sprintf("%s %s com motor de %d HP", c.Marca, c.Modelo, c.Motor.Potencia)
}

func main() {
    motor := Motor{Potencia: 150}
    carro := Carro{"Ford", "Mustang", motor}
    fmt.Println(carro.Detalhes())
}
