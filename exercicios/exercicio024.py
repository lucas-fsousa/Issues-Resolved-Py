#cidade = str(input("Digite o nome da sua cidade: ")).strip()
#cidade = cidade.lower()
#div = cidade.split()
#print(f"O nome da cidade comeca com a palavra santo?", "santo"in div[0])
#print("A cidade digita é: {}".format(cidade))

#------------------Simplificado-----------------

cd = str(input("Digite o nome da sua cidade: ")).strip()
print(f"O nome da cidade comeca com santo? ", cd[:5].upper() == "SANTO")