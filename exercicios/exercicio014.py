grau = float(input("Graus celsius: "))
fahr = (grau*9/5)+32
kelv = (grau+273.15)
print("{:.1f}°C convetidos equivalem a {:.1f}°F e {}K".format(grau, fahr, kelv))