from datetime import date
funci = {}
funci["nome"] = str(input("Nome: ")).strip().upper()
funci["nascimento"] = int(input("Ano de nascimento: "))
funci["idade-atual"] = date.today().year - funci["nascimento"]
sexo = ""
while sexo != "F" and sexo != "M":
    sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
resp = ""
while resp != "S" and resp != "N":
    resp = str(input("O colaborador {} possui carteita de trabalho? [S/N]: ".format(funci["nome"]))).upper().strip()[0]
    if resp != "S" and resp != "N":
        print("Resposta inválida. Tente novamente.")
if resp == "S":
    funci["ctps"] = int(input("Carteira de trabalho: "))
    funci["admissao"] = int(input("Ano de admissao: "))
    funci["salario"] = float(input("Salario contratual R$"))
    if sexo == "M":
        funci["Ano-Apos"] = funci["admissao"] + 65
    else:
        funci["Ano-Apos"] = funci["admissao"] + 62
    funci["Idade-Apos"] =  funci["Ano-Apos"] - funci["nascimento"]
print("\033[33m==========\033[m" * 6)
for i, k in funci.items():
    print(f" - {i}: {k}")
print("\033[33m==========\033[m" * 6)
