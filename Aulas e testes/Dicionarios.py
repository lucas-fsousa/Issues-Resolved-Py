#pessoas = {"nome": "Lucas", "sexo": "M", "idade": 22}
#print(pessoas["idade"])
#print("{} tem {} anos e é do sexo {}.".format(pessoas["nome"], pessoas["idade"], pessoas["sexo"]))

#for k, v in pessoas.items():
#    print(f"Utilizando o ITEMS: {k} = {v}")
#print("==========")
#for c in pessoas.keys():
#    print(f"Utilizando o KEYS: {c}")
#print("==========")
#for c in pessoas.values():
#    print(f"Utilizando o VALUES: {c}")
#print("==========")

#del pessoas["sexo"]     #Apaga o item entre colchetes.

#pessoas["nome"] = "Lucian"      #Declara um novo valor para o item nome.
#pessoas["peso"] = 98.5      #Adiciona um novo elemento ao dicionário.

#==========================================================================

#brasil = []
#estado = {"uf": "Rio de Janeiro", "sigla": "RJ"}
#estado01 = {"uf": "Sao Paulo", "sigla": "SP"}
#brasil.append(estado)
#brasil.append(estado01)
#print(brasil[0]["uf"], "-", brasil[0]["sigla"])

#========================================================================

estado = {}
brasil = []
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: ")).lower().strip()
    estado["sigla"] = str(input("Sigla: ")).lower().strip()[:2]
    brasil.append(estado.copy())
for e in brasil:
#    for k, v in e.items():
#        print(f"O campo {k} tem o valor {v}.")
    for v in e.values():
        print(v, end=" ")
    print()

