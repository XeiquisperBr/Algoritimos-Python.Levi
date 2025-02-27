def calcular_preco_final(preco_total, desconto_percentual):
    desconto = (preco_total * desconto_percentual) / 100
    preco_final = preco_total - desconto
    return preco_final

# Exemplo de uso
preco_final = calcular_preco_final(18, 9) # Desconto de 10% sobre 1000
print(preco_final) # Saída: 900.00
