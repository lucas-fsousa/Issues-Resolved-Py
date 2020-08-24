def area(la, co):
    res = la * co
    print(f"A área {la}x{co} é de {res:.2f}m²")
    print("\033[33m-=-\033[m" * 10)

#principal
print("-=-" * 10)
print("    Controle de terrenos")
print("-=-" * 10)
la = float(input("LARGURA (metros): "))
co = float(input("COMPRIMENTO (metros): "))
area(la, co)
