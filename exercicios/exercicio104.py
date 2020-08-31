def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input("Digite um numero: "))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mErro. Digite um numero inteiro\033[m.")
        if ok == True:
            break
    return valor
n = leiaint("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}!")