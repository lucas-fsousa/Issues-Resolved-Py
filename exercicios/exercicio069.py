mulhermenor = homem = pessoasmaior = 0
while True:
    idade = int(input("Qual a idade? "))
    sexo = str(input("Qual o sexo? [M/F] ")).strip().upper()
    if sexo != "M" and sexo != "F":
        while sexo != "F" and sexo != "M":
            sexo = str(input("Qual o sexo? [M/F] ")).strip().upper()
    if sexo == "F":
        if idade < 20:
            mulhermenor = mulhermenor + 1
    if idade > 18:
        pessoasmaior = pessoasmaior + 1
    if sexo == "M":
        homem = homem + 1
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if resp != "N" and resp != "S":
        while resp != "N" and resp != "S":
            resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
    print("\033[35m=-=\033[m" * 10)
    if resp == "N":
        break
print(f"Houveram {pessoasmaior} maiores de 18, com {homem} homens cadastrados e {mulhermenor} mulheres menores de 20 anos!")
print("\033[33m=========\033[m" * 10)
