c = ("\033[m",
    "\033[41m",
    "\033[36;42m",
    "\033[43m",
    "\033[44m",
    "\033[45m",
    "\033[7;30m"
     )
def ajuda(search):
    from time import sleep
    titulo(f"Acessando o manual de {search}", 4)
    sleep(0.6)
    print(c[6], end="")
    help(search)
    print(c[0], end="")

def titulo(msg, cor=0):
    tamanho = len(msg) + 2
    print(c[cor], end="")
    print("~" * tamanho)
    print(f" {msg}")
    print("~" * tamanho)
    print(c[0], end="")

comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYHELP!", 2)
    comando = str(input("Funcao ou Biblioteca |>>> ")).lower().strip()
    if comando == "fim":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)

