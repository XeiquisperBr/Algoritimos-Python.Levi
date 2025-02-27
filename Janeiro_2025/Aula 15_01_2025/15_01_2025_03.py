operacao = input("Digite a operação que deseja realizar (+, -, *, /, %)")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = primeiro_numero + segundo_numero
    operacao_nome = "Soma"
elif operacao == '-':
    resultado = primeiro_numero - segundo_numero
    operacao_nome = "Subtração"
elif operacao == '*':
    resultado = primeiro_numero * segundo_numero
    operacao_nome = "Multiplicação"
elif operacao == '/':
    resultado = primeiro_numero / segundo_numero if segundo_numero != 0 else "Erro: Divisão por zero"
    operacao_nome = "Divisão"
elif operacao == '%':
    resultado = primeiro_numero % segundo_numero
    operacao_nome = "Resto da divisão"
else:
    resultado = "Operação inválida"
    operacao_nome = ""

if resultado != "Operação inválida": 
    print(f'O resultado da {operacao_nome} entre {primeiro_numero} e {segundo_numero} é: {resultado}')
else:
    print("Operacao inválida. Tente novamente.")



# :\n","Mais: +\n","Menos: -\n","Vezes: *\n","Dividir /\n","Resto da divisão: %\n