import datetime
nome = str(input("Entre com seu nome: "))
idade = int(input("Entre com sua idade: "))
if idade < 18:
    falta = 18 - idade
    print("Olá, {}! Voce tem {} anos e \033[34mainda lhe restam {} anos\033[m até o alistamento!".format(nome, idade, falta))
elif idade == 18:
    print("Olá, {}! \033[33mjá está na hora de se alistar\033[m. Compareca a junta de servico militar mais proxima.".format(nome))
else:
    passou = idade - 18
    print("Olá, {}! Voce deveria ter se alistado aos 18 anos. Devido a excedencia de \033[31m{} anos\033[m para se alistar, será multado.".format(nome, passou))
