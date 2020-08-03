print("---------------")
print("----TABUADA----")
print("---------------")
n = int(input("Digite um numero: "))
print("Certo, já entendi!")
print("=="*7)
tot = 0
for c in range(0, 11, 1):
    tot = n * c
    print("{:2} x {:2} = {:2}".format(n, c, tot))
print(f"=="*7)