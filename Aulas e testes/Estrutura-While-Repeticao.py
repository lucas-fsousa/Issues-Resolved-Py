#--------------------------------Aplicacao do While---------------------------

#for c in range (1, 10):
#    print(c)
#print("FIM")
#--------------------------------------------------------------------------

#cont = 0
#while cont <= 10:
#    print(cont)
#    cont = cont + 1
#print("FIM")

#--------------------------------------------------------------------------

#resposta = "s"
#while resposta == "s":
#    num = int(input("Digite um numero: "))
#    resposta = str(input("Quer continuar? [S/N]: ")).lower()
#print("FIM")

#-------------------------------------------------------------------------

impar = 0
par = 0
c = 1
while c != 0:
    c = int(input("Digite um numero: "))
    if c != 0:
        if c % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print("Ao todo foram {} numeros impares e {} numeros  impares".format(impar, par))
print("FIM!")