"""
  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
 descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randrange, choice, randint

# inicío
print("Jogo da Adivinhação v.1.0", '-'*24) #26


# sorteando número
# sor = randrange(0, 6) # método 1
# sor = choice([0, 1, 2, 3, 4, 5]) # método 2, não muito bom
sor = randint( 0, 5) # método 3, Guanabara
print(f"\n\t\t*** Número entre 0 e 5 SORTEADO ***\n")

# entrada de tentativa
n = int(input("Digite um número entre 0 e 5: "))

# resultado
print("\n~ Resultado", '-'*38)

# condições de vitória e derrota
if n == sor :
    print("\n\t!!! PARABÉNS - VOCÊ GANHOU! !!!")
else :
    print(f"\n\tUma pena... Você perdeu! O Número sorteado era {sor}.")

# fim
print("\n-- FIM --")