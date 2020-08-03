from datetime import date
maior = 0
menor = 0
for c in range(0, 7, 1):
    ano = int(input("Digite o ano do nascimento: "))
    res = date.today().year - ano
    if res >= 21:
        maior = maior + 1
    elif res >= 0 and res < 21:
        menor = menor + 1
    else:
        print("Voce digitou um valor \033[31minválido\033[m!")
print("\033[36m==\033[m"*16)
print("{} pessoas sao \033[33mmaiores\033[m de idade!".format(maior))
print("{} pessoas sao \033[35mmenores\033[m de idade!".format(menor))
print("\033[36m==\033[m"*16)
