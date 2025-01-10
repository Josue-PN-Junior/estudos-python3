def aumentar(n=0, taxa=50, dinheiro=False):
    res = n + (n * taxa/100)
    if dinheiro:
        res = moeda(res)
    return res


def diminuir(n=0, taxa=50, dinheiro=False):
    res = n - (n * taxa/100)
    if dinheiro:
        res = moeda(res)
    return res


def dobro(n=0, dinheiro=False):
    res = n * 2
    if dinheiro:
       res = moeda(res)
    return res


def metade(n=0, dinheiro=False):
    res = n / 2
    if dinheiro:
       res = moeda(res)
    return res

def moeda(res=0):
    resultado = f"R${res:.2f}"
    resultado = resultado.replace('.', ',')
    return resultado

