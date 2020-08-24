base = []
alunos = []
individual = []
while True:
    nome = str(input("Nome: ")).upper().strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append(nome), individual.append(nota1), individual.append(nota2), alunos.append(media)
    alunos.append(individual[:])
    individual.clear()
    base.append(alunos[:])
    alunos.clear()
    resp = ""
    while resp != "s" and resp != "n":
        resp = str(input("Quer continuar? [S/N]: ")).lower().strip()[0]
    if resp == "n":
        break
print("\033[33m==========================\033[m" * 2)
print("          BOLETIM OLINE - CONSULTA GERAL")
print("\033[33m==========================\033[m" * 2)
for i, a in enumerate(base):
    print(f"ALUNO:\033[33m {a[0]}\033[m - MÉDIA: \033[33m{a[1]:.2f}\033[m - NOTAS SEMSTRAIS: \033[33m{a[2]}\033[m.")
while True:
    print()
    resp = str(input("Deseja buscar a nota indivual de algum aluno? [S/N]: ")).lower().strip()[0]
    if resp == "s":
        al = str(input("Nome: ")).upper().strip()
        for a in base:
            if a[0] == al:
                print(f"O aluno \033[33m{a[0]}\033[m teve média \033[33m{a[1]}\033[m e notas semestrais \033[33m{a[2]}\033[m")
    elif resp == "n":
        break
    else:
        print("Resposta \033[31mINVALIDA\033[m. Tente novamente.")
print("\033[35m================\033[m" * 4)
print("================ FIM DO PROGRAMA ================")
