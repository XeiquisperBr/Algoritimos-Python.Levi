idade = int(input("Digite a sua idade: "))

if idade >= 101:
    print("Hora extra né consagrado(a)?")
elif idade >= 65 and idade <= 100:
    print("Idoso")
elif idade >= 18 and idade <= 64:
    print("Adulto")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 0 and idade <= 12:
    print("Criança")
else:
    print("Digite uma idade válida.")