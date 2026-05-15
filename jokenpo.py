import random

while True:
    op = ["pedra", "papel", "tesoura"]

    pc = random.choice(op)

    # o pc vai escolher aleatoriamente
    jog = input("pedra, papel ou tesoura? ")

    if jog == "sair":
        print("saindo")
        break

    print(f"computador escolheu {pc}")

    if jog == pc:
        print("empate")

    elif jog == "pedra" and pc == "tesoura":
        print("você venceu")

    elif jog == "tesoura" and pc == "papel":
        print("você venceu")

    elif jog == "papel" and pc == "pedra":
        print("você venceu")

    else:
        print("computador venceu")