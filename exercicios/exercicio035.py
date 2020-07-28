print(f"-+-"*12)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
print(f"-+-"*12)
if r1 < (r2 + r3) and r2 < (r3 + r1) and r3 < (r2 + r1):
    print("Os numeros podem gerar um triangulo")
else:
    print("Impossivel gerar um triangulo")
print(f"-+-"*12)