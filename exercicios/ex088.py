"""
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
 gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
palpitesMega = list()
palpite = []
print("~ Palpites para a Mega Sena", '-'*22)
qt = int(input("> Quantos jogos quer gerar? "))

for j in range(1, qt+1):
    cont = 0

    while True:
        valor = randint(1, 60)
        if valor not in palpite:
            cont += 1
            palpite.append(valor)
        if cont == 6:
            break
    palpite.sort()
    palpitesMega.append(palpite[:])
    palpite.clear()

print("~ Resultado", '-'*38)
for j in range(0, qt):
    sleep(1)
    print(f"{j+1:3}º Palpite: {palpitesMega[j]}")
    print(" -  "*13)
print("\n{:^50}".format("*** BOA SORTE! ***"))