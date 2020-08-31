from utilidades import moedas
preco = float(input("Digite o preco do produto R$"))
print(f"A metade de {moedas.formatmoeda(preco)} é {moedas.formatmoeda(moedas.metade(preco))}")
print(f"O dobro de {moedas.formatmoeda(preco)} é {moedas.formatmoeda(moedas.dobro(preco))}")
print(f"O preco {moedas.formatmoeda(preco)} com 12% de aumento é R${moedas.formatmoeda(moedas.percentmax(preco, 12))}")
print(f"O preco {moedas.formatmoeda(preco)} reduzido em 33% é {moedas.formatmoeda(moedas.percentmin(preco, 33))}")
