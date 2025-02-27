lista =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("Índices positivos:")
for i in range(len(lista)):
    print(f"Índice {i}: {lista[i]}")

print("\nÍndices positivos:")
for i in range(-1, -len(lista)-1, -1):
    print(f"Índice {i}: {lista[i]}")

    