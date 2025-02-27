def criar_multiplicador (n):
    # Retorna uma função lambda que multiplica um número por n
    return lambda x: x*n

#Criando uma função que multiplica por 3
multiplicar_por_3 = criar_multiplicador(3)

# Usando a função lambda
print(multiplicar_por_3(5)) #Saída: 15