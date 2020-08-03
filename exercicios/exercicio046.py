from time import sleep
print("Olá! A queima de fogos vai comecar assim que voce der OK!")
print("\033[33m=-=\033[m"*22)
for c in range(2, -1, -1):
    assinatura = str(input("Deseja iniciar a contagem regressiva? Para iniciar digite OK: ")).lower().strip()
    if assinatura == "ok":
        print("\033[33m=-=\033[m" * 22)
        for c in range(10, -1, -1):
            print("Restam \033[35m{} segundos\033[m para a queima de fogos ".format(c))
            sleep(1.0)
        print("\033[33m=-=\033[m" * 13)
        print("\033[31mPOW\033[m! \033[32mPOW!\033[m \033[36mPOPOROPOPOW\033[m \033[32mPEEEW!\033[m \033[34mPEW! POOW\033[m!")
        break
    else:
        print("Usuario nao autenticado! Queima de fogos cancelada.")
        print("Lhe restam {} tentativas!".format(c))
print("\033[33m=-=\033[m" * 13)
