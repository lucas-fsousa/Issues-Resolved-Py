palavras = ("Aprender", "Python", "Gratis", "Curso", "Video",
            "Aproveite", "Para", "Virar", "Programador", "Experiente",
            "Mercado", "Trabalho")
for p in palavras:
    print(f"\nNa palavra {p.upper()} existem as vogais: ", end="")
    for letra in p:
        if letra.upper() in "AEIOU": # Mostrará se existe os caracteres em parenteses.
            print(letra.upper(), end=" ")
