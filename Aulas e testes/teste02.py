print(f"--------------------------")
print(f"Operadores Aritiméticos")
print(f"--------------------------")
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
div = n1/n2
som = n1+n2
mut = n1*n2
sub = n1-n2
pot = n1**n2
res = n1%n2
divi = n1//n2
print("A soma do números {} com o numero {} é: {}!".format(n1, n2, som))
print("A divisao do números {} por {} é: {}!".format(n1, n2, div))
print("A multiplicacao do números {} por {} é: {}!".format(n1, n2, mut))
print("A subtracao do números {} por {} é: {}!".format(n1, n2, sub))
print("{} elevado a {} potencia é: {}".format(n1, n2, pot))
print("A divisao inteira de {} por {} é: {}!".format(n1, n2, divi))
print("O resto da divisao de {} por {} é: {}!".format(n1, n2, res))