# Função que soma dois números
def somar(a, b):
    return a + b

# Função que subtrai dois números
def subtrair(a, b):
    return a - b

# Função que multiplica dois números
def multiplicar(a, b):
    return a * b

# Função que divide dois números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."
    
#Função principal que chama as operações matamáticas
def calcular():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o numero da operação: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = somar(num1, num2)
    elif escolha =='2':
        resultado = subtrair(num1, num2)
    elif escolha =='3':
        resultado = multiplicar(num1, num2)
    elif escolha =='4':
        resultado = dividir(num1, num2)
    else: 
        resultado = "Operação inválida!"
    print(f"Resultado: {resultado}")
    #Chama função principal
calcular()

