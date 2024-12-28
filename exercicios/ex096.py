"""
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
 retangular (largura e comprimento) e mostre a área do terreno.
"""
def area(l, c):
    area = l * c
    print(f"* Uma area com {l}m de largura e com {c}m de comprimento tem {area}m² ")


# __ Programa Principal __
print("~ Função que calcula área", '-'*14)
lar = float(input("Qual é a largura da parede? "))
com = float(input("Qual é o comprimento da parede? "))
print("~ Resultado", '-'*38)
area(lar, com)