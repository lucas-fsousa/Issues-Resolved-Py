lista = []
impar = []
par = []
while True:
    lista.append(int(input("Digite um numero: ")))
    resp = ""
    while resp != "s" and resp != "n":
        resp = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if resp == "n":
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f"A lista completa é {lista}.")
print(f"A lista de numeros pares é {par}.")
print(f"A lista de numeros impares é {impar}.")
