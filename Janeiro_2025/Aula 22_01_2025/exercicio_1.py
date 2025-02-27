nota = float(input("Digita a nota (0 a 100): "))

if nota >= 80 and nota <= 100:
    print("A nota é A")
elif nota >= 60 and nota <= 79:
    print("A nota é B")
elif nota >= 40 and nota <= 59:
    print("A nota é C")
elif nota >= 20 and nota <= 39:
    print("A nota é D")
elif nota >= 10 and nota <= 19:
    print("A nota é E")
elif nota == 0 and nota <= 10:
    print("A nota é F")
else:
    print("Digite uma nota válida.")