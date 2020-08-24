#Funcoes
def linha(txt):
    print("\033[33m-=-\033[m" * 17)
    print(txt)
    print("\033[33m-=-\033[m" * 17)
def soma(* valores):
    somar = 0
    for numero in valores:
        somar += numero
    print(f"Somando os valores {valores} temos um total de {somar}!")
    print("\033[33m-=-\033[m" * 10)
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

#==============================
#valores = [6, 3, 6, 1, 8, 15]
#dobra(valores)
#print(valores)
#==============================

soma(11, 5, 1)
