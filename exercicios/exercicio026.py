nome = str(input("Digite uma frase? ")).strip().upper()
print(f"A letra -A- aparece", nome.count("a"), "x no total.")
print(f"A letra -A- aparece pela primeira vez na posicao ", nome.find("a")+1)
print(f"A letra -A- aparece pela ultima vez em ", nome.rfind("a")+1)