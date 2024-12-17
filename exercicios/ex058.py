"""
  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
 foram necessários para vencer.

"""
from random import randint
print("~ Jogo da Adivinhação v2.0", '-'*23)
sorteado = randint(0, 10)
print("="*50)
print(f"\033[33m{"N Ú M E R O - S O R T E A D O - ( DE 0 A 10 )":^50}\033[m")
print("="*50)
num = int(input("Tente adivinhar o número sorteado: "))
tent = 1
if num != sorteado :
    while num != sorteado:
        if num < sorteado :
            print("Mais...")
        elif num > sorteado :
            print("Menos...")
        num = int(input("Você errou! Tente novamente: "))
        tent += 1
    print(f"\n* Parábens! Você acertou em {tent} tentativas!")
else :
    print(f"\n* UAU! Parábens! Você acertou de PRIMEIRA!")

