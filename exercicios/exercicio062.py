print("Gerador de PA!")
print("-="*10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("Progressao finalizada com {} termos apresentados.".format(total))
