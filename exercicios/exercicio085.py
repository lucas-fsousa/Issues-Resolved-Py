lista = [[], []]
for c in range(1, 8):
    n = int(input(f"Digite o {c}° numero: "))
    lista.append(n)
    if n % 2 == 0:
        lista[0].append(n)
        lista[0].sort()
    elif n % 2 == 1:
        lista[1].append(n)
        lista[1].sort()
print("\033[33m========\033[m" * 8)
print(f"Os numeros pares em ordem crescente sao {lista[0]}.")
print(f"e os numeros impares em ordem crescente sao {lista[1]}.")
print("\033[33m========\033[m" * 8)
