#classe base para representar um funcionario
class funcionario:
    def __init__(self, nome, salario_base):
     self.nome = nome
     self.salario_base = salario_base

    def calcular_salario(self):
        #Metodo comum que pode ser sibrescrito nas subclasses, mas não é abstrato.
        return self. salario_base
    
    def __str__(self):
        return f"Funcionario:{self.nome}, Salario: R${self.calcular_salario():.2f}"
    
#Subclasse para Gerentes
class gerente(funcionario):
    def __init__(self, nome, salario_base, bonus):
        funcionario.__init__(self, nome, salario_base) # Construtor da classe base
        self.bonus = bonus

    def calcular_salario(self):
        #O salario do gerente é o salario base + bonus
        return self.salario_base + self.bonus

#Subclasse para Analistas
class analista(funcionario):
    def __init__(self, nome, salario_base, horas_extra):
        funcionario.__init__(self, nome, salario_base) #Construtor da classe base
        self.horas_extra = horas_extra

    def calcular_salario(self):
        #o salario do analista é o salario base + pagamento por hora extras
        return self.salario_base + (self.horas_extra * 50) #exemplo: R$50 por hora extra