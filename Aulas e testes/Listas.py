num = [2, 5, 9, 1]      #Uma lista é representada por Colchetes!
print(f"Numeros da lista: {num}")
num[2] = 18     #As listas sao mutaveis e nessa linha o 9 recebeu o valor 18
print(f"Acrescentando o valor 18 no lugar do valor da posticao 3 {num}")

#================ADICIONANDO ITENS A UMA LISTA=======================

num.append(7)   #Vai adicionar o numero 7 ao final da lista
print(f"Acrescentando um novo valor a lista {num}")
num.sort()  #Colocara os numeros em ordem crescente
print(f"Atualizando a lista para ficar em ordem crescente {num}")
num.sort(reverse=True)  #Colocara os numeros em ordem decrescente.
print(f"Lista atualizada em ordem decrescente! {num}")
print(f"A lista tem ao todo {len(num)} elementos. Utilizando a funcao LEN para contar.")
num.insert(2, 0)    #Na posicao 2 incluirá o valor 0.
print(f"Utilizando a funcao insert() foi acrescentado o valor 0 na posicao 2. {num}")

#==================REMOVENDO ITENS DE UMA LISTA===========================

num.pop()   #Remove o ultimo valor de uma lista.
print(f"Utilizando a funcao pop o ultimo valor da lista foi removido. {num}")
num.pop(2)     #Vai remover o numero que está na posicao 3
print(f"Utilizando a funcao pop, foi removido o valor da posicao 3 {num}")

listagem = [1, 2, 3, 4, 5]
print(f"Um nova lista criada para testar o remove. {listagem}")
listagem.insert(2, 3)   #Insercao do valor 3 na posicao 2
print(f"Foi inserido o valor 3 na posicao 2 {listagem}")
listagem.remove(3)  #Remocao do primeiro valor 3 encontrado na lista
print(f"Utilizando o remove, que comeca a buscar o item desde a posicao 0, somente o primeiro a ser encontrado sera removido {listagem}")
for c, v in enumerate(listagem):    #Usando o enumerate será mostrada a posicao de cada elemento da lista.
    print(f"na posicao {c} foi encontrado o valor {v}...")
print(f"Cheguei ao final da lista.")

#=========UTILIZANDO O FOR PARA CRIAR UMA LISTA COM VALORES INTEIROS INPUTADOS==========
valores = list()
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
print(f"O valores digitados foram {valores}")

#==========================================================

a = [1, 2, 3, 4]
b = a[:]    # B vai receber todos os valores de A
#b = a #Cria uma ligacao com A
print(f"Lista A: {a}")
print(f"Lista B: {b}")
