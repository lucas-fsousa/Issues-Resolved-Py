frase = str(input("Digite um polindromo! ")).strip().lower()
frase = frase.replace(" ", "")
inverso = frase[::-1]
if frase == inverso:
    print("A frase {} é um palindromo! O inverso dela é {}".format(frase, inverso))
else:
    print("A frase {} nao é um palindromo!".format(frase))
print("\033[33m=====\033[m"*20)
