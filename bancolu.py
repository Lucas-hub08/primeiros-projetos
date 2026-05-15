s_correta = "123"

while True:

    senha = input("Digite a senha: ")

    if senha == s_correta:
        print("Login feito com sucesso")
        print("\n=== Bancolu ===\n")

        saldo = int(input("Qual é o seu saldo? "))

        while True:

            op = int(input(
                "Escolha uma opção:\n"
                "1 - Ver saldo\n"
                "2 - Depositar\n"
                "3 - Sacar\n"
                "4 - Sair\n"
            ))

            if op == 1:
                print(f"Seu saldo é de {saldo}")

            elif op == 2:
                depositar = int(input("Quanto você quer depositar? "))

                if depositar <= 0:
                    print("Digite um valor válido")

                else:
                    saldo += depositar
                    print(f"Você depositou {depositar} e agora seu saldo é {saldo}")

            elif op == 3:
                sacar = int(input("Quanto você deseja sacar? "))

                if sacar <= 0:
                    print("Digite um valor válido")

                elif sacar > 500:
                    print("Limite de saque é 500")

                elif sacar > saldo:
                    print("Saldo insuficiente")

                else:
                    saldo -= sacar
                    print(f"Você sacou {sacar} e agora seu saldo é de {saldo}")

            elif op == 4:
                print("Até logo")
                break

            else:
                print("Opção inválida")

        break

    else:
        print("Senha incorreta")
        