l1 = float(input("Digite o tamanho da lateral: "))
l2 = float(input("Digite o tamanho da outra lateral: "))
l3 = float(input("Digite o tamanho da ultima lateral: "))
if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2):
    print("Pode formar um triangulo!")
    if l1 == l2 == l3:
        print("Formará um triangulo EQUILATERO!")
    elif l1 != l2 != l3 != l1:
        print("Formará um triangulo ESCALENO!")
    else:
        print("Formará um triangulo ISÓSCELES!")
else:
    print("Nao pode formar um triangulo!")