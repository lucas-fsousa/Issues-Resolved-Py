from random import randint
print("\033[34m=-=\033[m" * 10)
print("  VAMOS JOGAR PAR OU IMPAR")
print("\033[34m=-=\033[m" * 10)
contvjog = contvpc = pc = somar = 0
pipc = ""
pi = ""
res = ""
rank = "JUVENIL"
while True:
    jogador = int(input("Diga um valor: "))
    pc = randint(0, 10)
    somar = pc + jogador
    pi = str(input("Escolha P para par e I para impar. [P/I]? ")).upper().strip()
    if pi == "P":
        pi = "PAR"
        pipc = "IMPAR"
    elif pi == "I":
        pi = "IMPAR"
        pipc = "PAR"
    else:
        while pi != "P" and pi != "I":
            pi = str(input("Escolha P para par e I para impar. [P/I]? ")).upper().strip()
    if somar % 2 == 1:
        res = "IMPAR"
    else:
        res = "PAR"
    if pi == res:
        contvjog = contvjog + 1
        if contvjog == 1:
            rank = "INICIANTE"
        elif contvjog == 2:
            rank = "IMPLACAVEL"
        elif contvjog == 3:
            rank = "MESTRE"
        else:
            rank = "LENDARIO"
    else:
        contvpc = contvpc + 1
    print("\033[34m=-=\033[m" * 15)
    if contvpc > 0:
        break
    print(f"O pc escolheu {pc} e o jogador {jogador} que totaliza {somar} e é {pi}")
    print(f"O Jogador se tornou \033[36m{rank}\033[m")
    print("\033[33m=-=\033[m" * 10)
print(f"O jogador perdeu após {contvjog} vitórias consecutivas e seu maior rank foi \033[31m{rank}\033[m!")
print("\033[33m=-=\033[m" * 26)
