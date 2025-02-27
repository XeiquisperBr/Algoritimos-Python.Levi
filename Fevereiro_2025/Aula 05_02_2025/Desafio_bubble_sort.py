# O Bubble sort pode ser otimizado?
# Sim, é possível otimizar o Bubble sort adicionando uma variável para verificar se houve trocas na última passagem. Se não houver trocas, 
# significa que a lista já está ordenada e o algoritmo pode ser interrompido.

lista = [64, 34, 25, 12, 22, 11, 90] # Lista de números a ser ordenado
indice = len(lista)

# Loop principal do Bubble Sort
for i in range(indice - 1):
    for j in range(indice - i -1):
        if lista[j] > lista[j+1]:
           
           # Troca os elementos de posição
            lista[j], lista[j+1] = lista[j+1], lista[j]

# Imprime a lista ordenada
print("Lista ordenada:")
for i in range(indice):
    print(lista[i], end=" ")