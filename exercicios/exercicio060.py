#--------------RESOLUCAO COM METODOS PRONTOS-------------

#from math import factorial
#from time import sleep
#cont = 0
#num = int(input("Digite um numero para saber seu fatorial: "))
#fatorial = factorial(num)
#print("Calculando...")
#sleep(2)
#print("O fatorial de {} é {}".format(num, fatorial))

#---------------RESOLUCAO MATEMATICA--------------------------
from time import sleep
n = int(input("Digite um numero para saber seu fatorial: "))
c = n
f = 1
print("Calculando {}!... ".format(n), end="")
while c > 0:
    sleep(0.6)
    if c == 1:
        print("{} = ".format(c), end="")
    else:
        print("{} x ".format(c), end="")
    f = f * c
    c = c - 1
print(f)
