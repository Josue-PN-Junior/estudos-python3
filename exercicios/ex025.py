"""
  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

# entrada
print("~ Procurando uma string dentro de outra", "-"*10) # 40 R12
nome = str(input("Qual é o seu nome completo? ")).strip()

# saída
print("~ Resultado", "-"*38)
nomes = nome.lower().split()
print(f"Seu nome tem Silva? {"silva" in nomes}")
