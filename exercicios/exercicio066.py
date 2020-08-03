s = c = numero = 0
while True:
    numero = float(input("Digite um numero ou [999] para sair!: "))
    if numero == 999:
        break
    s = s + numero
    c = c + 1
print(f"Foram digitados ao todo {c} numeros e a soma total foi de {s:.2f}.")
print("\033[33m===\033[m" * 30)
