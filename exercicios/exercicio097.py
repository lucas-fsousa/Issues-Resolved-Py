def escreva(msg):
    espc = (len(msg) + 4)
    print("\033[36m~\033[m" * espc)
    print(f"  {msg}")
    print("\033[36m~\033[m" * espc)


#Codigo principal

escreva("Only SAD")
