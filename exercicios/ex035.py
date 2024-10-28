"""
  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
  se elas podem ou não formar um triângulo.
"""

print("~ Analisando Triângulo v1.0", '-'*22) #28
rt1 = int(input("Comprimento da primeira reta: ")) # pode ser float também
rt2 = int(input("Comprimento da segunda reta: "))
rt3 = int(input("Comprimento da terceira reta: "))

print("~ Resultado", '-'*38)
# teste
if rt1 + rt2 < rt3 or rt1 + rt3 < rt2 or rt2 + rt3 < rt1 :
    print("\n* NÃO é possível formar um triângulo!")
else :
    print("\n* É POSSÍVEL formar um triângulo!")

# Método Guanabara
print("\nGuanabara diz:")
if rt1 < rt2 + rt3 and rt2 < rt1 + rt3 and rt3 < rt1 + rt2 :
    print("- Os segmentos PODEM FORMAR um triângulo!")
else :
    print("- Os segmentos NÃO podem formar um triângulo!")