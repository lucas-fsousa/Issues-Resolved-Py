from time import sleep
valores = []
cont = 0
while True:
    n = int(input("Digite um numero: "))
    if cont == 5 or cont == 10 or cont == 15 or cont == 20 or cont == 30:
        print("Para encerrar o fluxo, digite um \033[31mvalor negativo\033[m na próxima tentativa.")
    if n < 0:
        break
    cont = cont + 1
    if n not in valores:
        valores.append(n)
        print("Tsc... Tsc... Tsc... ")
        print(f"Parece que o valor {n} ainda nao esta na base. Um momento, estou adicionando...")
        sleep(0.9)
        print("\033[36mNumero cadastrado com sucesso\033[m.")
    else:
        print("Tsc... Tsc... Tsc... ")
        sleep(0.9)
        print(f"Este numero já está cadastrado em nossa base, portanto sera ignorado.")
    print("\033[33m========\033[m" * 10)
print(f"Os valores em ordem crescente sao: {sorted(valores)}")
