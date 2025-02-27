idade = int(input("Digite a sua idade (0 a 100) "))

if idade >=0 and idade<= 5:
    print("Menores que 5 anos tem entrada grátis.")
elif idade >= 5 and idade <= 12:
    print("O valor do seu ingreço é R$10,00")
elif idade >= 13 and idade <= 64:
    print("O valor do seu ingreço é R$20,00")
elif idade >= 65:
    print("O valor do seu ingreço é R$15,00")
else:
    print("Digite uma idade válida.")    
