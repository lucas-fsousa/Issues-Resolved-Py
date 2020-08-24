from random import randint
from time import sleep
jogos = []
listajogos = []
n = 0
valorjogo = 7.50

print("\033[33m===\033[m" * 15)
print("           \033[35mGANHA GANHA MEGA-SENA\033[m")
print("\033[33m===\033[m" * 15)
qtdjogos = int(input("Quantos jogos voce deseja fazer: "))
for c in range(0, qtdjogos):
    while len(jogos) < 6:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
            jogos.sort()
    listajogos.append(jogos[:])
    jogos.clear()
for i, jogo in enumerate(listajogos):
    print(f"Carregando o {i+1}° JOGO...")
    sleep(1)
    print(f"{i + 1}° JOGO: \033[36m{jogo}\033[m.")
    print("===================" * 2)
print(f"O valor a ser pago pelos jogos gerados é de R${qtdjogos * valorjogo:.2f}")
print("================== < BOA SORTE! > ==================")
