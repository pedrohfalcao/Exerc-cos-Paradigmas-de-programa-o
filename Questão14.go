package main

import (
    "fmt"
    sync "sync"
)

type Configuracao struct {
    config map[string]string
}

var instancia *Configuracao
var once sync.Once


func GetInstancia() *Configuracao {
    once.Do(func() {
        instancia = &Configuracao{config: make(map[string]string)}
    })
    return instancia
}

func (c *Configuracao) SetConfig(chave string, valor string) {
    c.config[chave] = valor
}

func (c *Configuracao) GetConfig(chave string) string {
    if valor, existe := c.config[chave]; existe {
        return valor
    }
    return "Configuração não encontrada"
}

func main() {
    config1 := GetInstancia()
    config1.SetConfig("url", "http://exemplo.com")

    config2 := GetInstancia()
    fmt.Println(config2.GetConfig("url")) 
    fmt.Println(config1 == config2)        
}
