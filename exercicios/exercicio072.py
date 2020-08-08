numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
           "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")
while True:
    resp = int(input("Digite um numero de 0 a 20 para le-lo por extenso: "))
    if resp > 20 or resp < 0:
        while resp > 20 or resp < 0:
            print(f"O valor {resp} nao é permitido! Tente algo entre 0 e 20.")
            resp = int(input("Digite um numero de 0 a 20 para le-lo por extenso: "))
    print(f"O valor digitado foi \033[33m{numeros[resp]}\033[m!")
    continuar = str(input("Quer continuar?[S/N] ")).lower().strip()[0]
    if continuar != "s" and continuar != "n":
        while continuar != "s" and continuar != "n":
            print("O valor digitado é Invalido. Tente novamente.")
            continuar = str(input("Quer continuar?[S/N] ")).lower().strip()[0]
    print("\033[36m===\033[m" * 20)
    if continuar == "n":
        break
print("---------Encerrou---------")

