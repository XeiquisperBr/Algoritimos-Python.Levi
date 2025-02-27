linha = '-' * 63

print('\n' + linha)
faturamento = int(input('Insira o faturamento mensal: '))
print('\n' + linha)
custo = int(input('Insira o custo mensal: '))

meta = 10000
print('\n' + linha)
print(f'O faturamento das vendas mensal foi de: R$ {faturamento - custo:,.2f}')

if faturamento > custo and meta >= faturamento:
    print('\n' + linha)
    print('      Sua empresa teve Lucro')
else:
    print('      Sua empresa teve Prejuízo')
    print('\n' + linha)

