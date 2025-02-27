# Exemplo de tratamento de erro em uma divisão
try:
    # Solicita ao usuário que insira dois números
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))

    # Realiza a divisão por inteiro
    resultado = numerador // denominador
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError as erro:
    # Este bloco será executado se o denominador for zero
    print(f"Erro: Não é possível dividir por zero. \n{erro}")

except ValueError as erro:
    # Este bloco será executado se a entrada não for um número inteiro
    print(f"Erro: Você deve inserir números inteiros.\n{erro}")