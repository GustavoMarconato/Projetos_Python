import random
numero_secreto = random.randint(1, 10)
tentativas = 0
while True:
    chute = int(input("Adivinhe o numero entre 1 e 10: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabens! Voce adivinhou o numero secreto em {tentativas} tentativas.")
        break
    # else:
    #     print("Tente novamente!")
    elif chute < numero_secreto:
        print("O numero secreto e maior. Tente novamente!")
    else:
        print("O numero secreto e menor. Tente novamente!")
  