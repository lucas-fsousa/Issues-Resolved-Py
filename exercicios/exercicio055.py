maior = 0
menor = 0
for c in range(0, 6, 1):
    peso = float(input("Qual o peso em (KG): "))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso é {}Kg".format(maior))
print("O menor peso é {}Kg".format(menor))
