peso = float(input("Entre com o peso (KG): "))
altura = float(input("Entre com a altura (MTS): "))
res = peso / (altura ** 2)
if res < 18.5:
    print("Seu IMC é {:.2f} e caracteriza sub-peso".format(res))
elif res >= 18.5 and res < 25:
    print("Seu IMC é {:.2f} e caracteriza Peso ideal".format(res))
elif res >= 25 and res < 30:
    print("Seu IMC é {:.2f} e caracteriza Sobrepeso".format(res))
else:
    print("seu IMC é {:.2f} e caracteriza Obesidade mórbida".format(res))
