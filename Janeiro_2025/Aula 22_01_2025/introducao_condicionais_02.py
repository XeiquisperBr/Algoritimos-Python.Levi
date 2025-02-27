idade = int(input("Digite sua idade: "))

tem_convite = str(input("Você tem um convite? (sim/não): ").strip().lower())

if idade >= 18:
    if tem_convite == "sim":
        print("Você pode entrar no evento.")
    else:
        print("Desculpe, você não pode entrar. É necessário ter um convite.")
    
else:
    if tem_convite == "sim":
        print("Desculpe você não pode entrar. Você precisa ser maior de 18 anos.")
    else:
        print("Desculpe, você não pode entrar. Você precisa ser maior de 18 anos e ter um convite")