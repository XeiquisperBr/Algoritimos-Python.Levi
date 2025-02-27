# Função fora de uma classe
def somar(a, b):
    return a + b

# Classe com um método
class Calculadora:
    def somar(self, a, b):
        return a + b
    
#Usando a função
resultado_funcao = somar(3,5)
print("Resultado da função:", resultado_funcao) #Imprime: 8

# Usando o método com a classe
calc = Calculadora()
resultado_metodo = calc.somar(3, 5)
print("Resultado do método:" , resultado_metodo) #Imprime: 8