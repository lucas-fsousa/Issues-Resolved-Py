import random
n1 = str(input("Digite o nome do aluno 01: "))
n2 = str(input("Digite o nome do aluno 02: "))
n3 = str(input("Digite o nome do aluno 03: "))
n4 = str(input("Digite o nome do aluno 04: "))
list = [n1, n2, n3, n4]
random.shuffle(list)
print("A ordem de escolha será", end=" ")
print(list)
