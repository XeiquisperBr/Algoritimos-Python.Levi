class Conta_Bancaria:
    def __init__(self, titular, saldo): # Atributos
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor): # Método
        self.saldo += valor
    
    def sacar(self,valor): # Método
        self.saldo -= valor

minha_conta = Conta_Bancaria("Levi", 100)

minha_conta.depositar(30)
minha_conta.sacar(200)

print(f'Seu saldo é: {minha_conta.saldo}')