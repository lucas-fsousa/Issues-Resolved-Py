#----------MINHA SOLUCAO------------
n = 0
print(f"=="*3)
for c in range(1, 51, 1):
    c = n+c
    if c % 2 == 0 and c < 10:
        print("| {}  |".format(c))
    elif c % 2 == 0 and c >= 10:
        print("| {} |".format(c))
print(f"=="*3)

#----------SOLUCAO DO PROFESSOR-------
for n in range(2, 51, 2): #vai pegar todos os pares e pular 2 numeros sem precisar contar de um em um
    print(n, end=" ")
print("ACABOU!")