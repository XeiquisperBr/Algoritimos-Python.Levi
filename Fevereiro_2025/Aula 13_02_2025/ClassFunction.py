class Cliente:
    def __init__(self, id_cliente, nome, endereco):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco
    
    def atualizar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} atualizado para {novo_endereco}.")
    
    def mostrar_dados(self):
        return f"Cliente {self.nome} ({self.id_cliente}), Endereço: {self.endereco}"

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
    
    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço do produto {self.nome} atualizado para R${novo_preco:.2f}.")
    
    def mostrar_dados(self):
        return f"Produto {self.nome} ({self.id_produto}), Preço: R${self.preco:.2f}"

class Pedido:
    def __init__(self, id_pedido, cliente, produtos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.produtos = produtos
    
    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)
    
    def mostrar_pedido(self):
        produtos_info = [produto.mostrar_dados() for produto in self.produtos]
        return f"Pedido {self.id_pedido} para {self.cliente.nome} ({self.cliente.id_cliente}):\n" + "\n".join(produtos_info)

def criar_cliente(id_cliente, nome, endereco):
    return Cliente(id_cliente, nome, endereco)

def criar_produto(id_produto, nome, preco):
    return Produto(id_produto, nome, preco)

def criar_pedido(id_pedido, cliente, lista_produtos):
    return Pedido(id_pedido, cliente, lista_produtos)

def mostrar_total_pedido(pedido):
    total = pedido.calcular_total()
    print(f"Total do Pedido {pedido.id_pedido}: R${total:.2f}")

def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente.mostrar_dados())

def listar_produtos(produtos):
    for produto in produtos:
        print(produto.mostrar_dados())

# Criando objetos
cliente1 = criar_cliente(1, "Leticia Souza", "Rua do pombo, 666")
cliente2 = criar_cliente(2, "Godoy", "Avenida das Bananas, 42")

produto1 = criar_produto(101, "Teclado Mecânico", 800.00)
produto2 = criar_produto(102, "Monitor LED", 1600.00)
produto3 = criar_produto(103, "Mouse Óptico", 100.00)

# Criando pedidos
pedido1 = criar_pedido(1001, cliente1, [produto1, produto2])
pedido2 = criar_pedido(1002, cliente2, [produto2, produto3])

# Exibindo informações
print(pedido1.mostrar_pedido())
mostrar_total_pedido(pedido1)

print("\n")

print(pedido2.mostrar_pedido())
mostrar_total_pedido(pedido2)

# Listando clientes e produtos
print("\nLista de Clientes:")
listar_clientes([cliente1, cliente2])

print("\nLista de Produtos:")
listar_produtos([produto1, produto2, produto3])

# Atualizando dados
cliente1.atualizar_endereco("Rua Nova, 789")
produto2.atualizar_preco(1150.00)
