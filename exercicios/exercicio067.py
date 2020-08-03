print("---------------")
print("----TABUADA----")
print("---------------")
tot = cont = n = 0
while True:
    print("\033[36m===\033[m" * 14)
    n = int(input("Qual tabuana voce quer ver? "))
    print("\033[36m===\033[m" * 14)
    if n < 0:
        break
    if n >= 0:
        for cont in range(1, 11, 1):
            tot = n * cont
            print(f"{n} x {cont} = {tot}!")
            cont = cont + 1
        print("\033[36m===\033[m" * 14)
        print("Para encerrar, digite um numero negativo!")
print("Voce digitou um valor de escape e a tabuada foi encerrada!!")
print("\033[36m====\033[m" * 15)
