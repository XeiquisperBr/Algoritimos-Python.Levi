class ContaBancaria:
    def __init__(self, saldo_inicial):
        #O salda é privado não pode ser acessado diretamente
        self.__saldo = saldo_inicial # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        # Permite o saque apenas se o valor for positivo
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        # Método público para retornar o saldo atual da conta.
        return self.__saldo
    
# Exemplo de uso da classe
conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)

print(conta.consultar_saldo())