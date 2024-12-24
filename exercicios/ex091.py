"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
 dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no
 dado.
"""
from random import randint
from time import sleep
jogada = dict()
resultado = list()
numMaior = numDado = 0

print("~ Jogo de Dados em Python", '-'*24)
for jog in range(1, 5):
    sleep(.5)
    numDado = randint(1, 6)
    print(f" @ Jogador{jog} tirou número {numDado}")
    jogada['jogador'] = f"Jogador{jog}"
    jogada['dado'] = numDado
    # adicona o primeiro item da lista
    if jog == 1:
        resultado.append(jogada.copy())
    else :
        # verifica se o dado atual é maior que o dado encontrado na lista
        # ele só vai adicionar o dado na lista se ele for mais que o atual verificado
        # caso não seja, ele continua até o final da lista
        # se no final ele não for maior que nem um registrado
        # ele é posto no final da lista
        # caso adiciona ele para o for
        for i, d in enumerate(resultado):
            if jogada['dado'] > d['dado']:
                resultado.insert(i, jogada.copy())
                break
            elif i == len(resultado)-1:
                resultado.append(jogada.copy())
                break

print("~ Resultado", '-'*38)
sleep(.7)
for p, j in enumerate(resultado):
    sleep(.5)
    print(f"* {p+1}º Lugar: {j['jogador']} com {j['dado']}")

# Guanabara
print("\n\nGuanabara Método: ")
from operator import itemgetter
jogo = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}
ranking = list()
for k, v in jogo.items():
    print(f" = {k} tirou {v}")
print("=-"*15)
print(f"{" RANKING ":^30}")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for p, j in enumerate(ranking):
    print(f"* {p+1}º lugar: {j[0]} com {j[1]} ")


