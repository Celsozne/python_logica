def menu():
    while True:
        try:
            print("Menu: ")
            print("1 - São múltiplos?")
            print("2 - São pares?")
            print("3 - A média entre os valores é maior ou igual a 7?")
            print("0 - Sair")
            opcao = input("Digite sua opção: ")

            if opcao == "1":
                multiplos()
            elif opcao == "2":
                pares()
            elif opcao == "3":
                media()
            elif opcao == "0":
                break
            else:
                print("Erro: digite uma opção válida")
        except ValueError:
            print("Erro: entrada inválida")


def multiplos():
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    if v1 % v2 == 0:
        print("São múltiplos")
    else:
        print("Não são múltiplos")

    input()
    menu()


def pares():
    v1 = float(input("Qual o primeiro valor: "))
    v2 = float(input("Qual o segundo valor: "))

    if v1 % 2 == 0 and v2 % 2 == 0:
        print(f"Os valores {v1}, {v2} são pares")
    elif v1 % 2 == 0 and v2 % 2 != 0:
        print(f"Apenas o valor {v1} é par")
    elif v1 % 2 != 0 and v2 % 2 == 0:
        print(f"Apenas o valor {v2} é par")
    else:
        print("Nenhum dos valores é par")

    input()
    menu()


def media():
    v1 = float(input("Qual o primeiro valor: "))
    v2 = float(input("Qual o segundo valor: "))

    m = (v1 + v2) / 2

    print(f"A média é {m}")

    input()
    menu()


if __name__ == "__main__":
    menu()
