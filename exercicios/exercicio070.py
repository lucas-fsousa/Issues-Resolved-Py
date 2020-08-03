preco = 0
totgasto = 0
c = 0
caro = 0
menor = 0
while True:
    nome = str(input("Nome do produto: "))
    valor = float(input("Valor do protudo R$"))
    print("\033[36m======\033[m" * 5)
    c = c + 1
    if c == 1:
        menor = valor
        nmenor = nome
    else:
        if valor < menor:
            menor = valor
            nmenor = nome
    if valor > 1000:
        caro = caro + 1
    totgasto = totgasto + valor
    resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if resp != "S" and resp != "N":
        while resp != "S" and resp != "N":
            resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    print("--------------------------------")
    if resp == "N":
        break
print("Cadastramento de protudos encerrado.")
print(f"O total gasto foi de R${totgasto:.2f}, houveram {caro} produtos com valor superior a R$1.000,00 e o mais barato foi {nmenor}.")