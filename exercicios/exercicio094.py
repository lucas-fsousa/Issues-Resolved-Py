pessoas = {}
lista = []
somaidade = media = 0
while True:
    pessoas["nome"] = str(input("Nome: ")).upper()
    pessoas["sexo"] = ""
    pessoas["idade"] = int(input("Idade: "))
    somaidade += pessoas["idade"]
    while pessoas["sexo"] != "M" and pessoas["sexo"] != "F":
        pessoas["sexo"] = str(input("Sexo [M/F]: ")).upper()
        if pessoas["sexo"] != "M" and pessoas["sexo"] != "F":
            print("Opcao \033[31minválida\033[m. Utilize apenas \033[33mF\033[m ou \033[33mM\033[m.")
    lista.append(pessoas.copy())
    resp = ""
    while resp != "N" and resp != "S":
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
        if resp != "N" and resp != "S":
            print("Resposta \033[31minválida\033[m.")
    if resp == "N":
        break
print("\033[36m-=-\033[m" * 15)
print(" [A] Pessoas cadastradas.")
print(f"      * \033[31m{len(lista)}\033[m")
media = somaidade / len(lista)
print(" [B] Média de idades.")
print(f"      * \033[35m{media:.2f}\033[m")
print(" [C] Pessoas do sexo feminino.")
for i, p in enumerate(lista):
    if p["sexo"] == "F":
        print("      * \033[33m{}\033[m".format(p["nome"]))
print(" [D] Pessoas com idade acima da média.")
for i, p in enumerate(lista):
    if p["idade"] > media:
            print("      * \033[34m{}\033[m - \033[37m{}\033[m anos do sexo \033[33m{}\033[m".format(p["nome"], p["idade"], p["sexo"]))
print("\033[36m-=-\033[m" * 15)
