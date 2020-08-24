jogador = {}
gols = []
jogador["Nome"] = str(input("Nome: ")).strip().upper()
partidas = int(input("Partidas jogadas: "))
for c in range(1, partidas + 1):
    gols.append(int(input(f"Quantidade de gols feitos no {c}° jogo: ")))
jogador["Gols"] = gols.copy()
jogador["total-gols"] = sum(gols)
print("\033[33m====\033[m" * 10)
print(jogador)
print("\033[33m====\033[m" * 10)
for k, v in jogador.items():
    print(f"O campo {k} possui o valor {v}")
print("\033[33m====\033[m" * 10)
print("O jogador {} jogou {} partidas: ".format(jogador["Nome"], len(jogador["Gols"])))
for c, i in enumerate(jogador["Gols"]):
    print(f"   No jogo {c+1} houve {i} gols.")
print("\033[33m====\033[m" * 10)
