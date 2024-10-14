class ContaBancaria:
    """Classe que representa uma conta bancária."""

    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular = titular
        self._saldo = saldo  

    def depositar(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Valor de depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Valor de saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self._saldo -= valor

    def get_saldo(self) -> float:
        return self._saldo


conta = ContaBancaria("João", 100)
conta.depositar(50)
try:
    conta.sacar(200)
except ValueError as e:
    print(e)  
