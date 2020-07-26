nome = str(input("Entre com o nome do produto: "))
valor = float(input("Entre com o valor do produto: R$"))
desc = float(input("Qual a porcentagem de desconto voce deseja aplicar: %"))
calcdes = desc*valor/100
valortot = valor-calcdes
print("O produto {} custa R${:.2f} e aplicando o desconto de {:.0f}% passara a custar R${:.2f}".format(nome, valor, desc, valortot))
