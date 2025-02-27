class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo = modelo #Atributo
        self.cor = cor                #Atributo
    
    def ligar(self):                  #Método
        print(f"O {self.modelo} de cor {self.cor} está ligado!")
    
    def desligar(self):               #Método
        print(f"O {self.modelo} de cor {self.cor} está desligado!")

    # Criando um objeto de classe carro
meu_carro = Carro("Fusca", "azul")

    # Acessandoi atributos
print(meu_carro.modelo) # "Fusca"
print(meu_carro.cor)    # "azul" 

# Cahmando métodos
meu_carro.ligar() #"Ofusca de cor azul está ligado"
meu_carro.desligar() #"Ofusca de cor azul está desligado"