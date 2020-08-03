somaidade = 0
maioridadehomem = 0
media = 0
mulheres = 0
idade = 0
sexo = ""
nome = ""
nomevelho = ""
for c in range(0, 4, 1):
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]: ")).lower()
    somaidade = somaidade + idade
    print("\033[36m===\033[m"*5)
    if c == 1 and sexo == "m":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "m" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo != "m" and idade <= 18:
        mulheres = mulheres + 1
media = somaidade/c
print("A média de idades é {}".format(media))
print("O homem mais velho se chama {} e tem {} anos.".format(nomevelho, maioridadehomem))
print("A existem {} mulheres menores de idade".format(mulheres))
print("\033[36m===\033[m"*15)