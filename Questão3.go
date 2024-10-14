package main

import (
    "errors"
    "fmt"
)

.
type ContaBancaria struct {
    Titular string
    saldo   float64 
}


func (c *ContaBancaria) Depositar(valor float64) error {
    if valor < 0 {
        return errors.New("valor de depósito deve ser positivo")
    }
    c.saldo += valor
    return nil
}


func (c *ContaBancaria) Sacar(valor float64) error {
    if valor < 0 {
        return errors.New("valor de saque deve ser positivo")
    }
    if valor > c.saldo {
        return errors.New("saldo insuficiente para saque")
    }
    c.saldo -= valor
    return nil
}


func (c *ContaBancaria) GetSaldo() float64 {
    return c.saldo
}
