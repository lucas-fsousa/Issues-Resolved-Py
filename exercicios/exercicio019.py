import random
aluno01 = str(input("Digite o nome do aluno 1: "))
aluno02 = str(input("Digite o nome do aluno 2: "))
aluno03 = str(input("Digite o nome do aluno 3: "))
aluno04 = str(input("Digite o nome do aluno 4: "))
lista = [aluno01, aluno02, aluno03, aluno04]
escolha = random.choice(lista)
print("{} foi escolhido(a) para apresentar o trabalho!".format(escolha))