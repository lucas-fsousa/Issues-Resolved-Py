largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
metragem = largura*altura
print("Sua parede tem a dimensao de {}x{} e area total de {}metros quadradados".format(largura, altura, metragem))
ltinta = 1/2
ttinta = ltinta*metragem
print("Voce precisara de {}l de tinta para pintar a area de {}mts quadrados!".format(ttinta, metragem))