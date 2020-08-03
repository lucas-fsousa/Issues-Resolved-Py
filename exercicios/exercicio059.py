from time import sleep
print(f"\033[33m==\033[m" * 12)
resp = 0
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
while resp != 5:
    print(f"\033[33m===\033[m" * 17)
    print("| [ 1 ] Para somar os numeros digitados.          |")
    print("| [ 2 ] Para multiplicar os numeros digitados.    |")
    print("| [ 3 ] Para ver o maior numero e o menor numero. |")
    print("| [ 4 ] Para digitar outros numeros.              |")
    print("| [ 5 ] Para Sair do programa.                    |")
    print(f"\033[33m===\033[m" * 17)
    resp = int(input("\033[4;35mRESPOSTA:\033[m "))
    if resp == 1:
        soma = n1 + n2
        print("A soma dos numeros é \033[36m{:.2f}\033[m".format(soma))
    elif resp == 2:
        mult = n1 * n2
        print("O numero \033[36m{:.2f}\033[m multiplicado por \033[36m{:2}\033[m é \033[36m{:.2f}\033[m!".format(n1, n2, mult))
    elif resp == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print("O numero {} é o maior e {} o menor!".format(maior, menor))
        elif n1 == n2:
            print("Os numeros {} e {} tem o mesmo valor!".format(n1, n2))
        else:
            menor = n1
            maior = n2
            print("O numero {} é o menor e {} o maior!".format(menor, maior))
        print("")
    elif resp == 4:
        print(f"\033[33m==\033[m" * 10)
        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))
    elif resp == 5:
        print(f"\033[33m==\033[m" * 16)
        print("Voce escolheu sair! Aguarde...")
        sleep(1.5)
    else:
        print("Opcao inválida! Tente digitar algo entre 1 e 5!")
print(f"\033[33m==\033[m" * 16)
print("ATÉ A PRÓXIMA!")
print(f"\033[33m==\033[m" * 7)
