from time import sleep
print("\033[33m=============\033[35m INTERNET BANKING \033[33m============\033[m")
print("\033[33m===========================================\033[m")
valor = int(input("Valor a ser sacado R$"))
total = valor
cedula = 100
totalcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalcedula = totalcedula + 1
    else:
        if totalcedula > 0:
            print(f"Total de {totalcedula} cédulas de R${cedula}")
            print("\033[31m---\033[m" * 9)
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalcedula = 0
        if total == 0:
            print("Contando cédulas. Aguarde!")
            print("Tsc... Tss... tss.. Tsc...")
            sleep(10)
            print("Retire o \033[32mdinheiro\033[m no local \033[33mindicado\033[m.")
            break
