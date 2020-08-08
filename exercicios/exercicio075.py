#MÉTODO PARA APLICAR MULTIPLOS NUMEROS DENTRO DE UMA TUPLA
num = (int(input("Digite um numero: ")),
       int(input("Digite outro numero: ")),
        int(input("Digite mais um numero: ")),
         int(input("Digite o ultimo numero: ")))
#==========================================================

print(f"Voce digitou os valores {num}")
print(f"O Valor 9 apareceu {num.count(9)} vezes")
if 3 in num:    #Se o 3 existir em numeros, entao:
    print(f"O valor 3 apareceu na posicao {num.index(3)+1}")
else:
        print("O 3 nao foi encontrado em nenhuma posicao!")
print("Sao numeros pares os numeros: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
print("\n=====================")