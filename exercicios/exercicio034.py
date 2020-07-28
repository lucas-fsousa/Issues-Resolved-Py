sal = float(input("Entre com o salario do funcionario: R$"))
aumento = int(input("Digite a porcentagem do aumento salarial: %"))
if sal > 1250:
    aumento = 3
    tot = sal+(aumento*sal/100)
    print("O seu salario era de R${:.2f} e esta acima da média, portanto o aumento é de 3% por padrao e passou a ser R${:.2f} no total".format(sal, tot))
else:
    if aumento < 5:
        aumento = 10
        print("A porcentagem de aumento digitado é inferior a 5%, portanto será definido como padrao 10%!")
    tot = sal+(aumento*sal/100)
    print("O seu salario era de R${:.2f} e com o aumento de {}% passou a ser R${:.2f}".format(sal, aumento, tot))