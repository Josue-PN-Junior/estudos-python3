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


def resumo(n, taxaA=50, taxaD=50, formato=False):
    print('- '*26)
    print(f"{f" Valor {moeda(n)} ":^50}")
    print('.'*50)
    print(f"{f"\tValor aumentando {taxaA}% ":-<30} {aumentar(n, taxaA, formato)}")
    print(f"{f"\tValor diminuindo {taxaD}% ":-<30} {diminuir(n, taxaD, formato)}")
    print(f"{f"\tValor dobrado ":-<30} {dobro(n, formato)}")
    print(f"{f"\tValor pela metade ":-<30} {metade(n, formato)}")
    print('- '*26)