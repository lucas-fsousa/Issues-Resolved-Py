num = int(input("Digite um numero inteiro: "))
print(f"\033[33m-=-\033[m"*16)
print(f"Escolha o numero que representa a base a ser convertida!")
print(f"Para Conversao Binaria: [1]")
print(f"Para Conversao Octal: [2]")
print(f"Para Conversao Hexadecima: [3]")
print(f"\033[33m-=-\033[m"*16)
escolha = int(input("Escolha: "))
if escolha == 1:
    print("{} convertido para binario é \033[36m{}\033[m!".format(num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertido para octal é \033[36m{}\033[m!".format(num, oct(num)[2:]))
elif escolha == 3:
    print("{} convertido para hexadecimal é \033[36m{}\033[m!".format(num, hex(num)[2:]))
else:
    print("Opcao inválida! Tente novamente.")
print(f"\033[33m-=-\033[m"*16)