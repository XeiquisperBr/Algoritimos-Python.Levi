import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100) # Sorteia um número entre 1 e 100
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação do MR. P")
    print("Eu, Mr P. estou pensando em um número entre 1 e 100. Tente adivinhar, se você adivinhar de primeira, você é um MAGO SUPREMO!")

    while True:
        palpite = int(input("Qual número é o seu palpite?"))
        tentativas += 1

        if tentativas == 1 and palpite == numero_secreto:
            print("Caaaaaaaaaaaraaca brother, acertou de primeira! Você é um insano MAGO SUPREMO!!!! Te saudo irmão!")
            break #Para o jogo, já venceu
        elif palpite < numero_secreto:
            print("O número é maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("O número é menor! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

adivinhar_numero()

#https://docs.python.org/pt-br/3.13/tutorial/index.html