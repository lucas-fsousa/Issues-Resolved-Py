def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero!
    :param num: Valor a ser calculado
    :param show: (Opcional) Mostrar o processo de contagem.
    :return: O valor do fatoriral de um numero!
    """
    from time import sleep
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            if c == num:
                print(f"{c}", end=" ")
            else:
                print(f"x {c}", end=" ")
            if c == 1:
                print("=", end=" ")
            sleep(0.5)
        f *= c

    return f

print(fatorial(7, True))

