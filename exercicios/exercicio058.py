from random import randint
n = 0
contador = 0
usuario = 0
win = False
print("Vamos jogar um jogo!", end=" ")
print("Vou pensar em um numero tente advinhar.")
while not win:
    n = randint(0, 10)
    usuario = int(input("Em que numero estou pensando? "))
    print("\033[33m===\033[m" * 20)
    contador = contador + 1
    if usuario != n:
        print("\033[34mO Mago é implacavel\033[m! Vamos de novo. Eu pensei no numero {}!".format(n))
    else:
        if contador > 3:
            print("Voce nao está a altura do \033[36mMAGO\033[m porque o \033[36mMAGO\033[m é \033[34mIMPLACAVEL\033[m!")
            print("O jogador precisou de {} tentativas. Tente melhorar!".format(contador))
        else:
            print("Voce ganhou com apenas {} tentativas.".format(contador))
            print("O jogador é \033[31mIMPLACAVEL\033[m!!")
        win = True
print("\033[33m===\033[m"*20)
