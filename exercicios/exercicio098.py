from time import sleep


def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print("\033[33m-=-\33[m" * 15)
    print(f"Contagem de {a} até {b} de {c} em {c}.")
    if a < b:
        cont = a
        while cont <= b:
            sleep(0.5)
            print(cont, end=" ")
            cont += c
        print("FIM.")
    else:
        cont = a
        while cont >= b:
            sleep(0.5)
            print(cont, end=" ")
            cont -= c
        print("FIM.")
    print("\033[33m-=-\33[m" * 15)
contador(10, 0, 2)
contador(1, 10, 1)
print("Agora é a sua vez de personalizar a contagem!")
a = int(input("Conte de: "))
b = int(input("Até: "))
c = int(input("Em passos de: "))
contador(a, b, c)
