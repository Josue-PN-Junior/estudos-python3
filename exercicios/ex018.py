"""
  Faça um programa que leia um ângulo qualquer e
 mostre na tela o valor do seno,
 cosseno e tangente desse ângulo.
"""
from math import tan, cos, sin, radians

# entrada
print("~ Seno, Cosseno e Tangente", "-"*23) #27+23=50 R12
angulo = int(input("Digite um ângulo: "))

# processamento
rad = radians(angulo) # tem que converter para radianos
seno = sin(rad)
cos = cos(rad)
tan = tan(rad)

# saída
print("~ Resultado", "-"*38)
print(f"O ângulo {angulo} tem o Seno de {seno:.3f}.")
print(f"O ângulo {angulo} tem o Cosseno de {cos:.3f}.")
print(f"O ângulo {angulo} tem a Tangente de {tan:.3f}.")