def maior(* num):
    maior = 0
    for c in num:
        if c > maior:
            maior = c
    print(f"Foram informados ao todo {len(num)} valores, sendo eles: ", end="")
    for c in num:
        print(c, end=" ")
    print("...")
    print(f"O numero {maior} é o maior entre os valores informados!")
    print("\033[33m-=-\033[m" * 25)

maior(1, 11, 17, 6, 3, 2)
maior()
