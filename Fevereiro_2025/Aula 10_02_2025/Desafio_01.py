# Cadastro de produtos:
# Crie um programa que permita cadastrar produtos em um estoque. 
# Para cada produto, armazene o nome, a quantidade e o preço unitário. O programa deve permitir:

# Adicionar novos produtos;
# Atualizar a quantidade de um produto existente;
# Remover produtos do estoque
#Exibir todos produtos cadastrados;

# estoque = {}

# nome = input('insira um produto:')
# quantidade = int(input('insira a quantidade:'))
# preco = float(input('insira o valor:'))

soma = 0

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")

    if numero.lower() == 'sair':
        break

    try:
        numero = float(numero)
        soma += numero
    except ValueError:
        print("Por favor, digitemum número válido.")

print(f"Asoma dos números digitados é: {soma}")