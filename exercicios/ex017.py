'''
  Faça um programa que leia o comprimento do cateto oposto e
 do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa.
 '''
from math import hypot, sqrt

# entrada
print("~ Catetos e Hipotenusa", "-"*27) #23+27=50
ct_opo = float(input("Comprimento do cateto oposto: "))
ct_adj = float(input("Comprimento do cateto adjacente: "))

# processamento
# hipotenusa = hypot(ct_opo, ct_adj)
'''# Calculo normal
hipotenusa = sqrt( (ct_opo * ct_opo) + ( ct_adj * ct_adj ) )
'''

# saída
print("~ Resultado", "-"*38)
print(f"A hipotenusa é: {hipotenusa:.4f}")