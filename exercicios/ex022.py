"""
  Crie um programa que leia o nome completo de uma pessoa e mostre:
 – O nome com todas as letras maiúsculas e minúsculas.
 – Quantas letras ao todo (sem considerar espaços).
 – Quantas letras tem o primeiro nome.
"""

print("~ Analisador de Textos", "-"*27) #t22 r12
#entrada de nome
nome = str(input("Qual é o seu nome completo? ")).strip()

# saída
print("~ Resultado", "-"*38)
print("Em maiúsculo:", nome.upper())
print("Em minuscúlo:", nome.lower())
# calculos de letras
"""
# metodo 1
ctr = int(len(nome))
spc = int(nome.count(' '))
ltr = ctr - spc
print("Quantidade de letras o nome possuí:", ltr, "letras")
"""
# metodo 2
nome_corte = nome.split() # corta em listas os nomes
nome_junto = "".join(nome_corte) # junta tudo sem espaços
ltr = len(nome_junto) # conta

# saída das quantidade letras
print("Quantidade de letras o nome possuí:", ltr, "letras")


# primeiro nome letras
print("Quantidade letras no primerio nome: ", len(nome_corte[0]), "letras")