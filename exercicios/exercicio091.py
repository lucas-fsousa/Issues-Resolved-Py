from random import randint
from time import sleep
from operator import itemgetter
jogadores = {"Jogador 1": randint(0, 6),
             "jogador 2": randint(0, 6),
             "jogador 3": randint(0, 6),
             "jogador 4": randint(0, 6)}
ranking = []
print("Valores sorteados: ")
for k, v in jogadores.items():
    print(f"{k} tiou {v} no dado.")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("\033[33m===\033[m" * 15)
print("                RANKING GERAL")
print("\033[33m===\033[m" * 15)
for i, v in enumerate(ranking):
    print(f"Em {i+1}° lugar ficou o {v[0]} com {v[1]} pontos no dado.")
    sleep(1)
print("Encerrou!")
