import math
angulo = float(input("Entre com valor do angulo a ser pesquisado: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Para o angulo de {:.0f} o seno é {:.2f}, o cosseno {:.2f} e a tangente é {:.2f}".format(angulo, seno, cosseno, tangente))