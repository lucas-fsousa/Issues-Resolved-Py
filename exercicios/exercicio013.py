nome = input("Entre com o nome do funcionario: ")
salbt = float(input("Salario bruto em R$"))
porc = float(input("Qual a porcentagem do aumento que sera aplicado: %"))
upsal = salbt+(salbt*porc)/100
sdcto = upsal*1/100
fgts = upsal*8/100
inss = upsal*8/100
saliq = upsal-(sdcto+fgts+inss)
print("O colaborador {} possui salario bruto de R${:.2f} e com o aumento de {:.1f}% passou a ser R${:.2f}".format(nome, salbt, porc, upsal))
print("Aplicando todos os descontos legais o salario liquido sera de R${:.2f}".format(saliq))

