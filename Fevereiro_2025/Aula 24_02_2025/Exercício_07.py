def registrar_pedido(id_cliente, itens, total_pedido):
    print(f"Pedido registrado para o cliente {id_cliente}:")
    print(f"Itens: {itens}")
    print(f"Total do pedido: R${total_pedido:.2f}")

# Exemplo de uso
itens_pedido = [{"produto": "Camiseta", "quantidade": 2}, {"produto": "Calça", "quantidade": 1}]
registrar_pedido(3457, itens_pedido, 150.00)