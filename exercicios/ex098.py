"""
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
 Seu programa tem que realizar três contagens através da função criada:
 a) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada
"""
from time import sleep


def contador(i, f, p):
    if p <= 0 :
        if p == 0:
            p = 1
        else :
            p = p * -1
    print(f"\n- Contagem de {i} até {f}, pulando de {p} em {p}!", end="\n\t> ")
    if i <= f:
        for c in range(i, f+1, p):
            print(f"{c} ", end="")
            sleep(0.3)
    else :
        for c in range(i, f-1, -p):
            sleep(0.3)
            print(f"{c} ", end="")
    print("FIM!")
    print("-" * 50)
    sleep(.5)


# __ Programa Principal __
print("~ Função de Contador", '-'*21)
contador(1, 10,1)
contador(10, 0, 2)
print("! Agora! Faça você a sua contagem! ")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print("~ Resultado", '-'*38)
contador(inicio, fim, passo)
print("Programa encerrado...")