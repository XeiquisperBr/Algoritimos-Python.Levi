from abc import ABC, abstractmethod

class FormaGeometrica (ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura)
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)