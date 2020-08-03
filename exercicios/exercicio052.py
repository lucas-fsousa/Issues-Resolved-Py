#----------RESOLUCAO 1------------
#from random import randint
#print("\033[34m=-=\033[m"*10)
#for c in range(0, 10, 1):
#    n = randint(1, 50)
#    if (n % 2) != 0 and (n % 3) != 0:
#        print("O numero {} é um numero primo!".format(n))
#print("\033[34m=-=\033[m"*10)

#----------RESOLUCAO 2 -----------
num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[35m", end="")
        tot = tot + 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
print("\n\033[mO numero {} foi divido {} vezes".format(num, tot))
if tot == 2:
    print("Por isso ele é primo.")
else:
    print("Por isso ele nao é primo.")
