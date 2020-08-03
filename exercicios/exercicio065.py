soma = media = cont = n = maior = menor =0
resp = "s"
while resp != "n":
    n = int(input("Digite um numero: "))
    resp = str(input("Quer continuar? [S/N]: ")).lower().strip()
    cont = cont + 1
    soma = n + soma
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if resp != "s" and resp != "n":
        print("Nao reconheco esta opcao. Tente novamente.")
        resp = "s"
media = soma / cont
print("A média foi {:.2f} de um total de {} numeros digitados!".format(media, cont))
print("O maior numero digitado foi {} e o menor foi {}.".format(maior, menor))
