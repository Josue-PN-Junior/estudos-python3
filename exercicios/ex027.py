"""
 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

# entrada
print("~ Primeiro e último nome de uma pessoa", '-'*11) #39
nome_completo = str(input("Nome completo: ")).title().strip()

# processamento
nome_separado = nome_completo.split()

# saída
print("~ Resultado", '-'*38)
print(f"Nome completo: {nome_completo}")
print(f"Primeiro nome: {nome_separado[0]} ")
print(f"Último nome: {nome_separado[len(nome_separado)-1]}")