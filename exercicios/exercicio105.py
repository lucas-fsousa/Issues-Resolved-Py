def notas(*nota, sit=False):
    """
    -> Funcao para analisar multiplas notas simultaneas
    :param nota: Uma ou mais notas, aceita multiplas
    :param sit: Valor opcional indicando se deverá acrescentar a situacao
    :return: Dicionario com informacoes.
    """
    r = {}
    r["total"] = len(nota)
    r["maior"] = max(nota)
    r["menor"] = min(nota)
    r["media"] = sum(nota) / len(nota)
    if r["media"] < 5:
        situacao = "Ruim"
    elif r["media"] >= 7:
        situacao = "Boa"
    else:
        situacao = "Intermediaria"
    if sit == True:
        r["situacao"] = situacao
    return r

resp = notas(4.4, 5.7, 10, sit=True)
print(resp)
