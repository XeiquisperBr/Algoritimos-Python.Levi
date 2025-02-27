import datetime

'Exemplo F-String'
faturamento_mensal = 3000
print(f'O faturamento mensal é de: R$ {faturamento_mensal:.2f}')
print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}')

print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}' .replace(',', 'X').replace('.',',').replace('X', '.'))

'Exemplo format'
nome = "Levi"
idade = 32
print("Nome: {}, Idade: {}".format(nome, idade))

print(f'O faturamento mensal é de: R$ {faturamento_mensal:.2f}')
print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}')

print(f'O faturamento mensal é de: R$ {faturamento_mensal:,.2f}' .replace(',', 'X').replace('.',',').replace('X', '.'))

'%d = dia' '%m = mês' '%y = ano'

data_atual = datetime.datetime.now()

data_formatada = f'A data de hoje é: {data_atual:%d/%m/%y}'
print(data_formatada)


valor = 5

if valor == 10:
    print("Os valores são iguais, que é:", valor)
elif valor != 5:
    print("Os valor é diferente da variável:", valor)

elif valor > 10:
    print("Os valor da variável é maior que o valor:", valor)

elif valor >= 10:
    print("Os valor da variável é maior ou igual:", valor)

elif valor < 5:
    print("Os valor da variável é menor:", valor)

elif valor <= 4:
    print("Os valor da variável é menor ou igual:", valor)
else:
    print("Esse valor nao existe")
