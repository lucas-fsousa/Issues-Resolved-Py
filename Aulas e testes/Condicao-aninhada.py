n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
s = (n1+n2)/2
if s > 8:
    print("Parabens voce teve um exelente desempenho e sua média é \033[4;36m{}\033[m.".format(s))
elif s >= 5 and s < 8:
    print("Se esforce um pouco mais, pois sua nota foi \033[4;35m{}\033[m e está na média.".format(s))
else:
    print("Voce foi reprovado! Precisa estar mais para melhorar a nota \033[4;31m{}\033[m e concluir a matéria.".format(s))
