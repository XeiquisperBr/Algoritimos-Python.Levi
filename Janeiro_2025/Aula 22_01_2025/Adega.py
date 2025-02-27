qtd_coca_cola = 500
qtd_pepsi = 500
preco_coca_cola = 4.50
preco_pepsi = 3.90
investimento_total = 6000.00
linha = '-' * 63

print('\n' + linha)
print(f'O total de latas de Coca Cola foi de: R$ {qtd_coca_cola * preco_coca_cola:,.2f}' + '\n')
print(f'O total de latas de Pepsi foi de:{qtd_pepsi * preco_pepsi:,.2f}')

faturamento = (qtd_coca_cola * preco_coca_cola) + (qtd_pepsi * preco_pepsi)

print(linha + '\n')
print(f'O faturamento das vendas de latas de refri foi de: R$ {faturamento - investimento_total:,.2f}' + '\n')

if investimento_total > faturamento:
    print(linha + '\n')
    print('          A empresa levou prejuízo nas vendas de Refri')
    print('\n' + linha)
else:
    print(linha + '\n')
    print('          A empresa teve lucro nas vendas de Refri')
    print('\n' + linha)