jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    gols.clear()
    jogador["Nome"] = str(input("Nome: ")).strip().upper()
    partidas = int(input("Partidas jogadas: "))
    for c in range(1, partidas + 1):
        gols.append(int(input(f"Quantidade de gols feitos no {c}° jogo: ")))
    jogador["Gols"] = gols.copy()
    jogador["total-gols"] = sum(gols)
    time.append(jogador.copy())
    resp = ""
    while resp != "S" and resp != "N":
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
        if resp != "S" and resp != "N":
            print(f"A resposta \033[31m{resp}\033[m é inválida. Tente novamente.")
    if resp == "N":
        break
print()
print("      TABELA DE RESULTADOS GERAIS")
print("\033[33m====\033[m" * 10)
print("ID |     NOME     |  PARTIDAS  | GOLS")
print("----------------------------------------")
for i, j in enumerate(time):
    print("{:<2} | {: ^12} | {: ^10} | {:>4}".format(i+1, j["Nome"], len(j["Gols"]),
        sum(j["Gols"])))
    print("----------------------------------------")
while True:
    indiv = int(input("Para buscar por um jogador, digite o ID correspondente ou 0 para encerrar: "))
    if indiv > len(time) or indiv < 0:
        print("Jogador nao localizado.")
        print("-------------------------------")
    if indiv == 0:
        break
    for i, j in enumerate(time):
        if indiv == i+1:
            print("    NOME     |  PARTIDAS  | GOLS")
            print("-----------------------------------")
            print("{: ^12} | {: ^10} | {:>4}".format(i+1, j["Nome"], len(j["Gols"]), sum(j["Gols"])))
print("\033[33m====\033[m" * 30)
