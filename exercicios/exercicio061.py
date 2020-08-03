print("=-="*12)
print("----------TERMOS DE UMA PA----------")
print("=-="*12)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo = termo + razao
    cont = cont + 1
print(termo)
