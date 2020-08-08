#As tuplas sao representadas com parenteses. EX: variavelx = ("suco", "Abacate", "aviaao")
#Tuplas sao imutaveis.

#----------------------------------------------------------------

#lanche = ("Suco", "pizza", "pudim", "hamburguer") #Variavel composta

#print(lanche[-1]) # Mostrará o ultimo elemento. Usando numeros negativos é possivel comecar do fim.
#print(lanche[2:]) # Mostrará do objeto 2 até o final.
#print("-----------")

#------------------------------------------------------------

#for cont in range(0, len(lanche)):
#    print(f"Eu vou comer {lanche[cont]} na posicao {cont}")
#-----------------------------------------------
#for comida in lanche:
#    print(sorted(f"EU vou comer {comida}")) # O sorted mostra as coisas em ordem alfabetica.
#print("Comi para caramba!")

#------------------------------------------------


a = (2, 5, 4)   #Tupla A
b = (5, 8, 1, 2)    #Tupla B

c = a + b   # Tupla C juntará a tupla A + a tupla B. A ordem influencia
d = b + a   # Tupla D juntará a tupla B + a tupla A. A ordem foi afetada.

print("Tamanho da tupla C:", len[c])    #Mostrará o tamanho da tupla

print(f"Contagem de {c.count[9]}")  #Mostra quantas vezes aparece o 9 na tupla C

print(c.index(4))   #Mostra em que posicao está o numero 4; O index é a posicao.

print(c.index(5, 1))    #Mostra o primeiro 5 da lista a partir da posicao 1 // serve para procurar uma posicao aleatoria.

pessoa = ("Lucas", 21, "M", 80.50)  # A tupla aceita valores de tipos diferentes
del (pessoa) #Deleta uma tupla ou qualquer objeto.

print(a)
print("-------------------------")
print(b)
print("-------------------------")
print(c)
print("-------------------------")
print(d)
print("-------------------------")
#-----------------