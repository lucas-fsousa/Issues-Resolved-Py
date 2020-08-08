times = ("Corinthians", "Palmeiras", "Santos", "Gremio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atlétigo-PR", "Bahia", "Sao Paulo", "Fluminense", "Sport Recife",
         "EC Vitória", "Coritiba", "Avai", "Ponte Preta", "Atletigo-GO")
print("\033[33m===\033[m" * 10)
print("Lista de times do brasileirao!")
for lista in times:     #O contador servira para mostrar os times em individual
    print(lista)    #Mostra de 1 por 1
print("\033[33m======= OS 5 primeiros colocados =======\033[m")
print(f"{times[:5]}")
print("\033[33m======= OS 4 ultimos colocados =======\033[m")
print(f"{times[-4:]}")
print("\033[33m======= OS Times em ordem alfabética =======\033[m")
print(sorted(times))
print("\033[33m======= Posicao da chape =======\033[m")
print("A chape está na posicao", times.index("Chapecoense")+1) #o "+1" atualizará a posicao da chape que esta em 8 lugar, mas mostra apenas o 7


