from datetime import datetime


print("Olá mundo")

modelo = 'Ford'
print('O modelo do meu carro', modelo)

print('\n')
print("Eu amo estudar no Senac")
print('')

texto = "Por lei dirigir é permitido para maiores de:"
idade = 18
print(texto, idade)

print("Estou aprendndo Python!")

nome = "Godoy"
cidade = 'Sbo'
print("Meu nome é", nome, 'e eu moro em', cidade)

a = 5
b = 10
soma = a + b
print("A soma de", a,"e", b, "é", soma)

nome = "Levi"

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

data_atual = datetime.now()

data_formatada = f'Adatade hoje é: {data_atual:%d/%m/%y}'
print(data_formatada)
