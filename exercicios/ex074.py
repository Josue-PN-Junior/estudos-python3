"""
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
 de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
maiorNum = menorNum = 0
print("~ Maior e menor valores em Tupla", '-'*17)
numerosAletorios = (randint(1, 20), randint(1, 20), randint(1, 20),
                    randint(1, 20), randint(1, 20))
print(f"Números gerados: {numerosAletorios}")
print("~ Resultado", '-'*38)
for i, num in enumerate(numerosAletorios) :
    if i == 0 or num > maiorNum:
        maiorNum = num
        maiorI = i
    if i == 0 or num < menorNum :
        menorNum = num
        menorI = i
print(f"> O maior número da tupla é {maiorNum}, posição {maiorI}")
print(f"> O menor número da tupla é {menorNum}, posição {menorI}")
# usando max
print(f"> O maior valor sorteado foi {max(numerosAletorios)}")
print(f"> O menor valor sorteado foi {min(numerosAletorios)}")
