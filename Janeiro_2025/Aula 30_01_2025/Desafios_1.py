#Divisão por zero - Crie um programa que peça ao usuário para inserir dois números e realize a divisão entre eles. Use try e except para tratar a exceção de divisão por zero.
'''try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador:"))

    resultado = numerador // denominador
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError as erro:
     print(f"Erro: Não é possível dividir por zero.\n{erro}." )

except ValueError as erro:
    print(f"Erro: Você deve inserir numéros inteiros.\n{erro}" )'''

#Verificar se é um número - Crie um programa que peça ao usuário para inserir um número. Se o usuário digitar algo que não seja um número, trate a exceção com except.
'''try:
    numero = int(input("Digite um número: "))

except ValueError as erro:
    print(f"Você precisa digitar um número.\n{erro}")'''

#Acessar um índice da lista - Crie uma lista com 3 elementos. Peça ao usuário para acessar um índice da lista. Trate a exceção caso o índice informado não exista na lista.
    
lista = ['a', 'b', 'c']

indice = int(input("Digite um índice: "))
print(f"")