from random import randint
maior = menor = 0
tp = ()
a = b = c = d = e = 0
for cont in range(0, 5):
    n = randint(0, 10)
    if cont == 0:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    if cont == 0:
        a = n
    elif cont == 1:
        b = n
    elif cont == 2:
        c = n
    elif cont == 3:
        d = n
    else:
        e = n
print(f"Os numeros sorteados foram: \033[4;33m{a}, {b}, {c}, {d} e {e}\033[m!")
tp = (a, b, c, d, e)
print(f"O terceiro valor da tupla é: {tp[2]}")
print(f"O maior valor foi {maior} e o menor foi {menor}.")

#=============SOLUCAO DO PROFESSOR===================
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Foram sorteados os numeros: {n}")
print(f"O maior valor sorteado foi {max(n)}")   # O max() mostra o maior numero de uma variavel
print(f"O menor valor sorteado foi {min(n)}")   # o min() mostra o menor numero de uma variavel