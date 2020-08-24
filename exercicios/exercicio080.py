n = 0
lista = []
contador = 0
while contador < 9:
    n = int(input("Digite um numero: "))
    if contador == 0 or n > lista[-1]:      #Verifica e insere um objeto no primeiro e ultimo local
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    contador += 1
print(f"Os valores digitados foram {lista}")
