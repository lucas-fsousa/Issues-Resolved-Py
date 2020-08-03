print("=-="*12)
print("----------TERMOS DE UMA PA----------")
print("=-="*12)
termo = int(input("Termo: "))
razao = int(input("Razao: "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
     print("{} ->".format(c), end=" ")
print("Acabou!")
