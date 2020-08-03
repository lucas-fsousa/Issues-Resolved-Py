n = soma = cont = 0
n = int(input("Digite um numero! [999 encerra a contagem]: "))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input("Digite um numero! [999 encerra a contagem]: "))
print("Encerrou e o total somado é {}".format(soma))
