aluno = {}
base = []
aluno["nome"] = str(input("Nome: "))
nota1 = float(input("Nota 01: "))
nota2 = float(input("Nota 02: "))
resultado = (nota1 + nota2) / 2
if resultado < 5:
    aluno["media"] = resultado
    aluno["status"] = "Reprovado"
elif resultado >= 5 and resultado < 7:
    aluno["media"] = resultado
    aluno["status"] = "Recuperacao"
else:
    aluno["media"] = resultado
    aluno["status"] = "Aprovado"
base.append(aluno.copy())
for a in base:
    for i, v in a.items():
        print(f"{i} é {v}")

