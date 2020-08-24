def sorteia(valores):
    from random import randint
    from time import sleep
    print("Sorteando numeros --> ", end="")
    for c in range(0, 5):
        sorting = randint(1, 10)
        valores.append(sorting)
        sleep(0.6)
        print(sorting, end=" ")

    print("<-- Encerrou o sorteio")

def somapar(valores):
    pares = 0
    for c in valores:
        if c % 2 == 0:
            pares = pares + c
    print(f"A soma dos valores é {pares}.")
n = list()
sorteia(n)
somapar(n)