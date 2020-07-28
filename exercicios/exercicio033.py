from random import randint
n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
menor = n1
maior = n1
#-------------verificar o menor-----------
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
#-------------verificar o maior-----------
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
