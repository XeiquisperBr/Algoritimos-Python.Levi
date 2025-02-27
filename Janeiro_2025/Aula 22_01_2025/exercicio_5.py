mes_anivesario = int(input("Digite o mês do seu aniversário."))

if  mes_anivesario == 9 or mes_anivesario == 10 or mes_anivesario == 11:
    print("Você nasceu na primavera.")
elif mes_anivesario == 12 or mes_anivesario == 1 or mes_anivesario == 2:
    print("Você nasceu no verao.")
elif mes_anivesario == 3 or mes_anivesario == 4 or mes_anivesario == 5:
    print("Você nasceu no outono.")
elif mes_anivesario == 6 or mes_anivesario == 7 or mes_anivesario == 8:
    print("Você nasceu no inverno.")
else:
    print("Nasceu errado irmão(ã).")
    
    
    
#AND = uma ou outra condição
#OR = qualquer uma das condições