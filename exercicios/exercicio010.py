real = float(input("Quantos reais voce tem? R$"))
dol = real/5.21
eur = real/6.06
pa = real/0.07
ien = real/0.04

print("Voce consegue comprar USD${:.2f} com R${:.2f}!".format(dol, real))
print("Voce consegue comprar EUR${:.2f} com R${:.2f}!".format(eur, real))
print("Voce consegue comprar ARS${:.2f} com R${:.2f}!".format(pa, real))
print("Voce consegue comprar JPY${:.2f} com R${:.2f}!".format(ien, real))