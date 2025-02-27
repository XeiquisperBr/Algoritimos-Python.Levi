# Função lambda que soma dois números
soma = lambda a, b: a + b

resultado = soma(5, 3)
print(resultado) # Saíd: 8

#Função lambda que verifica se um número é par
par_impar = lambda x: "Par" if x % 2 == 0 else "Ímpar"

print(par_impar(4)) # Saída: Par
print(par_impar(7)) #Saída Ímpar