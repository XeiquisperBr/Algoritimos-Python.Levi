# Definindo uma classe com um método
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor

# Criando um objetto de classe Carro
meu_carro = Carro("azul", "sedan")

# Usando o método acelerar
meu_carro.acelerar(30)
print(meu_carro.velocidade) #Saída:30.