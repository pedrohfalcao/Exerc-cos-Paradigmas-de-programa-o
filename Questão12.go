package main

import "fmt"


type Produto struct {
    Nome  string
    Preco float64
}


func (p Produto) Combinar(outro Produto) Produto {
    return Produto{
        Nome:  p.Nome + " e " + outro.Nome,
        Preco: p.Preco + outro.Preco,
    }
}

func main() {
    produto1 := Produto{"Camiseta", 50.00}
    produto2 := Produto{"Calça", 100.00}
    produtoCombinado := produto1.Combinar(produto2)
    fmt.Printf("Produto combinado: %s - R$%.2f\n", produtoCombinado.Nome, produtoCombinado.Preco)
}
