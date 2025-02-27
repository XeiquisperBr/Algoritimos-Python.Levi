# Definindo uma classe
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return "Som do Animal"
    
# Criando uma classe a partir da classe animal (Herança)
class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"
    
# Testando a classe cachorro
meu_cachorro = Cachorro("Amarelão", "Cachorro")
print(meu_cachorro.emitir_som()) # Saída: Au au!