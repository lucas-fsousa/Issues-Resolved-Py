import time
import random
print(f"Olá. Vamos jogar um jogo?")
nome = str(input("Me fale seu nome: "))
print(f"-=-"*10)
print(f"Pedra, Papel ou Tesoura?")
escolha = str(input("Escolha: ")).lower().strip()
escmaq = ["pedra", "papel", "tesoura"]
maquina = random.choice(escmaq)
if escolha == "pedra" or "papel" or "tesoura":
    print(f"-=-" * 10)
    print(f"\033[33mJooooo...\033[m", end="")
    time.sleep(1.4)
    print(f"\033[34m  keennnn...\033[m", end="")
    time.sleep(1.4)
    print(f"\033[36m  POOO!!\033[m")
    time.sleep(0.5)
    print(f"-=-" * 10)
    if escolha == "papel" and maquina == "pedra" or escolha == "pedra" and maquina == "tesoura" or escolha == "papel" and maquina == "pedra":
        print("{}, dessa vez voce \033[32mganhou\033[m porque eu escolhi \033[31m{}\033[m. Nos veremos na próxima rodada!".format(nome, maquina))
    elif escolha == maquina:
        print("Empatamos!")
    else:
        print("HAHAHAHA!! O computador escolheu \033[35m{}\033[m e \033[34mganhou O JOGO!!!\033[m".format(maquina))
else:
    print("Impossivel jogar! A opcao {} nao faz parte do jogo.".format(escolha))
print(f"Até a próxima.")
print(f"-=-" * 10)