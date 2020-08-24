menor = maior = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posicao {c}: ")))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print("\033[36m=-\033[m" * 30)
print(f"Os valores digitados foram {valores}.")
print(f"O maior valor foi {max(valores)} e está na posicao ", end="")
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f"{posicao}... ", end="")
print("")
print(f"O menor valor foi {min(valores)} e está na posicao ", end="")
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f"{posicao}... ", end="")
print("\nEncerrou")

