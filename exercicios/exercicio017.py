
cop = float(input("Valor do cateto oposto: "))
caj = float(input("Valor do cateto adjacente: "))
hip = (cop**2 + caj**2)**(1/2)
print("A hipotenusa vai medir {:.2f}m".format(hip))
print(f"")

#------------------MÉTODO II------------------------

import math
hi2 = math.hypot(cop, caj)
print(f"------------------MÉTODO II-------------------")
print(f"")
print("A hipotenusa vai medir {:.2f}m".format(hi2))