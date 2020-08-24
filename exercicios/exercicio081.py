r = ""
lista = []
while True:
    lista.append(int(input("Digite um numero: ")))
    r = ""
    while r != "s" and r != "n":
        r = str(input("Quer continuar? [S/N]: ")).strip().lower()[0]
    if r == "n":
        break
if 5 in lista:
    print("O numero 5 faz parte da lista!")
else:
    print("O numero 5 nao apareceu nenhuma vez.")
print(f"Foram digitados ao todo {len(lista)} numeros.")
lista.sort(reverse=True)
print(f"Segue a lista de forma decrescente. {lista}")
