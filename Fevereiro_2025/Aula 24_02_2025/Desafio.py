def calcular_imc (peso, altura):
    imc =  peso / (altura * altura) 
    return imc

imc = calcular_imc(69, 1.73)

print(f"{imc:.2f}")

if imc <= 18.5:
    print("Abaixo do peso.")

elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal.")

elif imc >= 24.9 and imc <= 29.9:
    print("Sobrepeso.")

elif imc >= 30 and imc <= 39.9:
    print("Obesidade.")

elif imc > 40:
    print("Obesidade Grave.")

else:
    print("Digite um valor válido")