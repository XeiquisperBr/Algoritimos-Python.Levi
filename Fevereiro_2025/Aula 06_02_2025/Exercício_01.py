produtos = []
precos = []
estoques =[]
vendas = []

print("Bem vindo ao maravilhoso sistema de estoque e vendas my friend!")
print("Aqui você vai poder adicionar seus produtinhos, inserir os preços, quantidade em estoque e também a quantidade de itens vendida, coisa fina man.")
print("Se quiser sair desse programinha filé basta deixar o nome do produto em branco e apertar o Enter, porém sabe que vai ficar com saudade pq o programa é dez!")

while True:
    nome_produto = input("\nDigite o nome do produto/item my friend(ou pressione enter diretão para sair, sentiremos sua falta!)")

    if nome_produto == "":
        break

    try:
        preco_produto = float(input(f"Qual o preço unitário my friend? {nome_produto}: R$"))

    except ValueError:
        print("Mermão digita número po.")
        continue

    try:
        estoque_produto = int(input(f"Digite a quantidade em estoque my friend do {nome_produto}: "))

    except ValueError:
        print("Mermão digita número inteiro po, tá moscando?")
        continue

    try:
        quantidade_vendida = int(input(f"Digite o tanto que você vendeu my friend do {nome_produto}: "))
    
    except ValueError:
        print("Mermão digita número inteiro po, tá moscando?")
        continue

    if nome_produto in produtos:

        index = produtos.index(nome_produto)
        estoques[index] += estoque_produto
        vendas[index] += quantidade_vendida
    else:
        produtos.append(nome_produto)
        precos.append(preco_produto)
        estoques.append(estoque_produto)
        vendas.append(quantidade_vendida)
    
valor_total_vendas = 0
produto_mais_vendido = None
maior_quantidade_vendida = 0

for i in range(len(produtos)):
    valor_vendas_produto = vendas[i] * precos[i]
    valor_total_vendas += valor_vendas_produto
