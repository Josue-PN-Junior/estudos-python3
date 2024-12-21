"""
    Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, mostre:
 A) Quantos números foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.
"""
print("~ Extraindo dados de uma Lista", '-'*19)
listaNumeros = list()
while True:
    listaNumeros.append(int(input("Digite um valor: ")))

    while True:
        resp = str(input("> Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        break

print("~ Resultado", '-'*38)
print(f"Lista: {listaNumeros}")
print(f"Ao todo foram informados {len(listaNumeros)} números")
listaNumeros.sort(reverse=True)
print(f"Lista com os valores em ordem drescente: {listaNumeros}")
if 5 in listaNumeros :
    print("O valor 5 está na lista!")
else :
    print("O valor 5 NÃO está na lista!")