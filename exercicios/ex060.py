"""
  Faça um programa que leia um número qualquer e mostre o seu fatorial.
 Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial

print("~ Cálculo do Fatorial", '-'*28)
num = int(input("Digite um número: "))
fat = 0
fatorial = 1
while fat != num :
    fat += 1
    fatorial = fatorial * fat

print("~ Resultado", '-'*38)
print(f"Fatorial de {num} é {fatorial}")
print(f"Verificando {factorial(num)}")