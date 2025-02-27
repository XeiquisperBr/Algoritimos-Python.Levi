pessoas = [("Levi", 32), ("Diego", 18), ("Alper", 22)]

# Ordenando pelo segundo elemento da tupla (idade)
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)
# Saída: [('Diego', 18), ('Alper', 22), ('Levi', 32)]