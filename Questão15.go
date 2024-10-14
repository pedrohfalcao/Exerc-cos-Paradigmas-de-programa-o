package main

import "fmt"


type Animal interface {
    EmitirSom() string
}


type Cachorro struct{}


func (Cachorro) EmitirSom() string {
    return "Au Au!"
}


type Gato struct{}


func (Gato) EmitirSom() string {
    return "Miau!"
}


func FazerSom(animal Animal) {
    fmt.Println(animal.EmitirSom())
}

func main() {
    var cachorro Animal = Cachorro{}
    var gato Animal = Gato{}

    FazerSom(cachorro) 
    FazerSom(gato)     }
