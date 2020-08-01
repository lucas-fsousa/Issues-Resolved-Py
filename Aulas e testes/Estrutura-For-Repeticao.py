#---Aplicando a estrutura de repeticao FOR------
#sintaxe em portugol
#for c in range(1, 6): ## O for vai ter como contador o "C" no intervalo de 1 a 6.

#------------------Aplicando--------------------

#for c in range(0, 6):
#    print("Hello Word!!")
#    print(c)
#print("FIM.")
#print("")
#print("-=-"*15)
#print("")

#---------------Contagem regressiva-------------

#for c in range(10, 0, -2): #O ultimo caractere é o numero que indica a quantidade de saltos
#    print(c)
#print("")
#print("FIM")

#----------------------------------------------

#Contagem com o usuario digitando um valor

#num = int(input("Digite um numero: "))
#for c in range(0, num+1):
#    print(c)

#----------------------------------------------

#contagem com complemento total do usuario

#inicio = int(input("Inicio: "))
#fim = int(input("Fim: "))
#passos = int(input("Passos: "))
#for c in range(inicio, fim+1, passos):
#    print(c)
#print("FIM")

#-------APLICANDO FOR COM QUESTIONAMENTO------
soma = 0
for c in range(0, 4 ):
    n = int(input(("DIgite um valor: ")))
    soma = soma + n
print("A soma dos valores é: {}".format(soma))
