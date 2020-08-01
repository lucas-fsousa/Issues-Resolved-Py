from datetime import date
nasc = int(input("Digite o ano de nascimento do atleta: "))
ano = date.today().year - nasc
if ano >= 0 and ano <= 9:
    print("Idade: {} - Categoria: \033[36mMirin\033[m.".format(ano))
elif ano > 9 and ano <= 14:
    print("Idade: {} - Categoria: \033[33mInfantil\033[m.".format(ano))
elif ano > 14 and ano <= 19:
    print("Idade: {} - Categoria: \033[32mJunior\033[m.".format(ano))
elif ano > 19 and ano <= 20:
    print("Idade: {} - Categoria: \033[34mSenior\033[m.".format(ano))
elif ano >20:
    print("Idade: {} - Categoria: \033[35mMaster\033[m.".format(ano))
else:
    print("Idade inválida. Voce nao veio do futuro!")
