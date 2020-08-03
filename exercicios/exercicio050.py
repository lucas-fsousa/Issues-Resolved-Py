from random import randint
s = 0
ntot = 0
for c in range(0, 6):
    n = randint(1, 100)
    print("Numero da vez: {}".format(n))
    if n % 2 == 0:
        s = s+n
        ntot = ntot+1
    else:
        print("==" * 20)
        print("|O numero {} é impar e nao sera somado!|".format(n))
        print("==" * 20)
print("a soma dos valores foi {} de um total de {} numeros somados.".format(s, ntot))