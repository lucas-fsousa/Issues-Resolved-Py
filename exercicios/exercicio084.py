pesada = leve = cont = 0
lista = []
geral = []
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso KG: ")))
    cont += 1
    geral.append(lista[:])
    lista.clear()
    resp = ""
    while resp != "n" and resp != "s":
        resp = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if resp == "n":
        break
for i, p in enumerate(geral):
    if p[1] <= 70:
        leve += 1
        print(f"{p[0]} tem {p[1]}kg ", end="")
print(f"que faz parte da faixa de menor peso.")
for i, p in enumerate(geral):
    if p[1] >= 90:
        pesada += 1
        print(f"{p[0]} tem {p[1]} ", end="")
print(f"que faz parte da faixa de maior peso.")
print(f"Foram cadastradas ao todo {cont} pessoas sendo... ", end="")
for i, p in enumerate(geral):
    if p[1] >70 and p[1] < 90:
        print(f"{p[0]} com {p[1]}kg ", end="")
print(f"na média de pesos.")
