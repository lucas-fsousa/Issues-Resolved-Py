preco = float(input("Qual o valor total? R$"))
print(f"-=-"*14)
print(f"FORMAS DE PAGAMENTO:")
print(f"Digite 1 para pagar á vista em dinheiro!")
print(f"Digite 2 para pagar á vista no cartao!")
print(f"Digite 3 para pagar em até 2x no cartao!")
print(f"Digite 4 para pagar em até 12x no cartao!")
print(f"-=-"*14)
opc = int(input("Selecione: "))
if opc == 1:
    preco = preco - (preco*10)/100
    print("Voce pagará R${:.2f}".format(preco))
elif opc == 2:
    preco = preco - (preco*5/100)
    print("Voce pagará R${:.2f}".format(preco))
elif opc == 3:
    print("Voce pagará R${:.2f}".format(preco))
elif opc == 4:
    preco = preco + (preco * 20) / 100
    qparc = int(input("Qunatas vezes? "))
    parcelas = preco / qparc
    print("Voce pagará R${:.2f} divido em {} parcelas de R${:.2f}".format(preco, qparc, parcelas))
else:
    print("Alternativa inválida!")
print(f"-=-"*10)
