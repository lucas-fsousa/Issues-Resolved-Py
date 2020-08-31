from utilidades import moedas
preco = float(input("Digite o preco do produto R$"))
print(f"A metade de R${preco} é {moedas.metade(preco)}")
print(f"O dobro de R${preco} é {moedas.dobro(preco)}")
print(f"O preco R${preco} com {12}% de aumento é R${moedas.percentmax(preco, 12)}")
print(f"O preco R${preco} reduzido em {33}% é {moedas.percentmin(preco, 33)}")
