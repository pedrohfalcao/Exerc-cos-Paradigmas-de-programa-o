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

func emitirSons(animais []Animal) {
    for _, animal := range animais {
        fmt.Println(animal.Som())
    }
}

func main() {
    animais := []Animal{Cachorro{}, Gato{}}
    emitirSons(animais) 
}
