"""
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
 A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint


def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 10))


def somaPar(lista):
    somaPar = contP = 0
    for v in lista:
        if v % 2 == 0:
            somaPar += v
            contP += 1
    if contP == 0:
        print("**Não foram encontrados valores pares...")
    else :
        print(f"* Soma dos PARES: {somaPar}")


# __ Programa Principal __


print("~ Funções para sortear e somar", '-'*19)
numeros = list()
sorteia()
print(f"Valores sorteados: {numeros}")
print("~ Resultado", '-'*38)
somaPar(numeros)