frase = str("  Bicicletinha turbinada de teste  ")

#-----------FATIAMENTO----------------
print(frase[4]) #vaimostrar o caractere 4
print(frase[2:6]) #vai mostrar do caractere 2 ao 5
print(frase[2:10:2]) #mostrara do caractere 2 ao 10 pulando 2 por vez

#---------------ANALISE---------------
print(len(frase)) #mostra a quantidade de caractere da frase
print(frase.count("c"))
print(frase.count("c", 4, 12))

#------------TRASNFORMACAO------------
print(frase.upper()) #transforma a frase em maiusculo
print(frase.capitalize()) #transforma a primeira letra da string inteira em maiscula
print(frase.title())#Transfrorma a primeira letra de cada palavra da string em maiuscula
print(frase.strip()) #remove os espacos desnecessarios de uma string
print(frase.rstrip()) #remove os espacos desnecessarios da direita

#--------------DIVISAO---------------
print(frase.split()) #trasnforma cada palavra da string geral em multiplas strins

#--------------JUNCAO----------------
print("-".join(frase))
