# Peça ao usuário o preço de um produto e a porcentagem de desconto. O programa deve calcular o valor de 
# desconto e o preço final do produto. 
# Caso a porcentagem informada seja maior que 100%, o programa deve exibir uma mensagem de erro.
linha = '-' * 63
valor_produto = float(input("Digite o valor do produto: "))
print(linha)
desconto = float(input("Digite a porcentagem de desconto: "))
print('\n' + linha)

resultado = (valor_produto * desconto) / 100

if desconto >= 0 and desconto <= 100:
    print(f"| Valor do produto: ${valor_produto:.2f} |".replace('.', ','))
    print(linha)
    print(f"| Porcentagem de desconto: {desconto}% |")
    print(linha)
    print(f"| Valor de desconto: ${resultado:.2f} |".replace('.', ','))
    print(linha)
    print(f"| Preço final: ${valor_produto - resultado:.2f} |".replace('.', ','))
    print(linha)

else:
    print("Digite um valor de desconto entre 1 e 100%!")
    print(linha)