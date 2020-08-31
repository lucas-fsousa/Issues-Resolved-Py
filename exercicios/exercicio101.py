def votar(anoNascimento):
    from datetime import date
    idade = date.today().year - anoNascimento
    if idade >= 16 and idade < 18 or idade >= 65:
        return f"A idade é {idade}: VOTO OPCIONAL!"
    elif idade < 16:
        return f"A idade é {idade}: NAO VOTA!"
    else:
        return f"A idade é {idade}: VOTO OBRIGATORIO!"

print(votar(1955))
