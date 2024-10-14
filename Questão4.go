package main

import "fmt"


type Animal interface {
    Som() string
}


type Cachorro struct{}


func (Cachorro) Som() string {
    return "Au Au"
}


type Gato struct{}


func (Gato) Som() string {
    return "Miau"
}

func emitirSom(animal Animal) {
    fmt.Println(animal.Som())
}

func main() {
    cachorro := Cachorro{}
    gato := Gato{}

    emitirSom(cachorro) 
    emitirSom(gato)     
}
