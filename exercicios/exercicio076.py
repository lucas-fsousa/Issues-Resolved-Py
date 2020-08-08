print("---" * 14)
print("           Listagem de precos")
print("---" * 14)
listagem = ("Lapis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f"{listagem[posicao]:.<30}", end="") # alinha o texto a esquerda e preenche os espacos com pontos
    else:
        print(f"R${listagem[posicao]:>7.2f}")    #  alinha o texto a direita com 2 casas flutuantes
print("---" * 14)
