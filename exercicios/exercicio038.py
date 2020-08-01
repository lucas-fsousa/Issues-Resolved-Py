n1 = float(input("Entre com um numero: "))
n2 = float(input("Entre com outro numero: "))
if n1 > n2:
    print("O numero {} é maior que o numero {}".format(n1, n2))
elif n2 > n1:
    print("O numero {} é menor que o numero {}".format(n1, n2))
else:
    print("Os numeros sao equivalentes!")
print("\033[36mAté a próxima!\033[m")
