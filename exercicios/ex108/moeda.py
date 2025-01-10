


def dobro(n=0):
    res = n * 2
    return res


def triplo(n=0):
    res = n / 2
    return res


def aumenta(n=0, taxa=50):
    res = n + (n * taxa/100)
    return res


def diminuir(n=0, taxa=50):
    res = n - (n * taxa/100)
    return res


def metade(n=1):
    res = n / 2
    return res


def moeda(n):
    m = str(f"R${n:.2f}").replace('.', ',')
    return m