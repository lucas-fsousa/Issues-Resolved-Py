matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o numero correspondente [{l}, {c}]: "))
print("===" * 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print("====" * 12)
print(f"A soma dos valores pares é {pares}.")
for l in range(0 , 3):
    somacoluna += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {somacoluna}.")
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f"O maior valor da coluna 1 é {maior}")

