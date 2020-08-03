contador = 1
while contador != 0:
    sexo = str(input("Digite seu sexo: ")).lower().strip()
    if sexo == "f":
        print(f"\033[33m===\033[m" * 10)
        print("Voce escolheu o sexo \033[31mFEMININO\033[m.")
        print(f"\033[33m===\033[m" * 10)
        contador = 0
    elif sexo == "m":
        print(f"\033[33m===\033[m" * 10)
        print("Voce escolheu o sexo \033[31mMASCULINO\033[m")
        print(f"\033[33m===\033[m" * 10)
        contador = 0
    else:
        print(f"\033[33m===\033[m" * 16)
        print("- Essa alternativa é \033[31minválida\033[m. Tente novamente -")
        print(f"\033[33m===\033[m" * 16)
print("Encerrou aqui.")
print(f"\033[33m===\033[m" * 5)