ex = str(input("Digite uma expressao: "))
pilha = []
for simbolo in ex:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao está válida.")
else:
    print("Sua expressao está inválida.")
