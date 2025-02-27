# Get consulta e Set altera
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome # Atributo privado
        self.__preco = preco #Atributo privado
    
    #Getter para o nome
    def get_nome(self):
        return self.__nome
    
    #Setter para o nome
    def set_nome(self, nome):
        self.__nome = nome
    
    # Getter para o preço
    def get_preco(self):
        return self.__preco
    
    # Setter para o preço
    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print("Preço inválido! O preço deve ser maior que 0.")
    
# Uso
produto = Produto("Camiseta", 50)

# Alterando o nome e o preço
produto.set_nome("Camiseta Estampada")
produto.set_preco(60)

# Acessando os atributos após a modificação
print("Novo nome do produto:", produto.get_nome())
print("Novo preço do produto:", produto.get_preco())

# Tentando definir um preço inválido
produto.set_preco(-10) # Saída: Preço inválido
