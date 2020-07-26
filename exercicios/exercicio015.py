dia = int(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos KM rodados no periodo: "))
skm = 0.15*km
sdia = 60*dia
tot = skm+sdia
print("Foram percorridos ao todo cerca de {:.0f}KM durante o periodo de {} dias que geraram um custo de R${:.2f}".format(km, dia, tot))
