print(f"\033[33m-=-\033[m"*15)
print(f"\033[36mSeja bem vindo a central de financiamento.\033[m")
print(f"\033[33m-=-\033[m"*15)
vlcasa = float(input("Entre com o valor da casa: R$"))
salario = float(input("Entre com seu salario liquido: R$"))
anos = float(input("Em quantos anos pretende pagar o financiamento? ")) * 12
parcela = vlcasa/anos
calcperc = (salario*30)/100
if parcela > calcperc:
    print(f"O financiamento nao podera ser concluido!")
    print("O valor de cada parcela é de \033[32mR${:.2f}\033[m e excede os \033[31m30%\033[m do seu salario que equivale a \033[32mR${:.2f}\033[m.".format(parcela, calcperc))
else:
    print(f"\033[4;34mParabens!\033[m Seu financiamento foi aceito com sucesso!")
    print("Voce pagará \033[4;32mR${:.2f}\033[m mensalmente e seu financimaneto foi concluido com \033[4;33m{:.0f}\033[m parcelas".format(parcela, anos))