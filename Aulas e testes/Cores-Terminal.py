#---------Aplicando cores-------------

#\033[Estilo de letra;cor-texto;Cor de fundoM

#----------Lista de numeracao para modificar a fonte---------

# 0 - Sem formato
# 1 - Aplicar o negrito
# 2 - Underline / sublinhado
# 7 - Inverte as configuracoes; Texti vira background e background vira texto

#---------Lista de numeracao para colorir o texto------------

# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Azul claro
# 37 - Cinza

#--------Numeracao para colorir o background -------------

# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Azul claro
# 47 - Cinza

#--------------------------------

##print(f"\033[0;31mTeste\033[m")

#-----------EXEMPLO PRATICO--------------

#nome = str(input("Digite seu nome: "))
#print("Olá {}{}{}! É um prazer conhecer voce.".format("\033[4;34m", nome, "\033[m"))

#------------CRIANDO O MODELO DE CORES----------

cores = {"cls": "\033[m", "az": "\033[34m", "am": "\033[33m", "ptbc": "7;30", "verm": "\033[31m", "verd": "\033[32m",
         "ro": "\033[35m", "azcl": "\033[36m"}
nome = str(input("Qual o seu nome? "))
print("Olá, {}{}{}! Tudo bem com voce?".format(cores["az"], nome, cores["cls"]))