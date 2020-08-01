n1 = float(input("Digite a nota 01: "))
n2 = float(input("Digite a nota 02: "))
n3 = float(input("Digite a nota 03: "))
m = (n1 + n2 + n3) / 3
if m >= 7 and m <= 10:
    print("O aluno teve a média {} e foi \033[34mAprovado\033[m".format(m))
elif m > 5 and m < 6.9:
    print("O aluno teve média {} e ficou de \033[32mRecuperacao!\033[m".format(m))
elif m >= 11 and m < 100:
    print("Verifique as notas, pois algo pode estar \033[31merrado\033[m!".format(m))
else:
    print("O aluno teve média {} e foi \033[31mReprovado\033[m".format(m))
