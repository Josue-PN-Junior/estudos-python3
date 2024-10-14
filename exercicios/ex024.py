"""
  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""
from os.path import split
from random import sample

# entrada
print("~ Verificando as primeiras letras de um texto", "-"*14) # 45+5 R12
cidade = str(input("Informe uma cidade: ")).strip()

# minha versão atualizada
c = cidade.lower()
c = c.split()
c = ("santo" in c[0] and (len(c[0]) == 5))

'''
# Guanabara version
# nesse 'santos' não funciona
print(cidade[:6].upper() == "SANTO")
'''

# saída
print("~ Resultado", "-"*47)
print(c)