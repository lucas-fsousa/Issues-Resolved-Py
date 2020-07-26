cidade = str(input("Digite o nome da sua cidade: "))
cidade = cidade.lower()
div = cidade.split()
print(f"O nome da cidade comeca com a palavra santo?", "santo"in div[0])
