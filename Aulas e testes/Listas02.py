#============================LISTAS EM PRATICA=======================
#pessoas = [["Pedro", 25], ["Maria", 19], ["Joao", 32]]
#print(f"Este é o item 0 que se encontra na posicao 0 de PESSOAS: \033[33m{pessoas[0][0]}\033[m.")
#print(f"Este é o item 1 que se encontra na posicao 1 de PESSOAS: \033[36m{pessoas[1][1]}\033[m.")
#print(f"Este é o item 2 que se encontra na posicao 0 de PESSOAS: \033[31m{pessoas[2][0]}\033[m.")
#print(pessoas[1])

#==================================================================
lista = []
geral = []
maior = menor = 0
for c in range(0, 5):
    lista.append(str(input("Digite seu nome: ")))
    lista.append(int(input("Digite sua idade: ")))
    print("\033[36m====\033[m" * 6)
    geral.append(lista[:])
    lista.clear()
print("===== Lista com pessoas =====")
print("")
for p in geral:
    if p[1] > 17:
        maior += 1
        print(f"Este(a) é \033[33m{p[0]}\033[m com \033[33m{p[1]}\033[m anos e é maior de idade!")
    else:
        menor += 1
        print(f"Este(a) é \033[31m{p[0]}\033[m com \033[31m{p[1]}\033[m anos e é menor de idade!")
print("")
print(f"Existem {maior} pessoas maiores de idade e {menor} pessoas menores de idade.")
print("=======" * 5)
