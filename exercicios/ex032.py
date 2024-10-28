"""
 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

# Início
print("~ Ano Bissexto", '-'*35) # 15
print("* Para o ano atual digite: 0")
ano = int(input("Informe um ano: "))

# ano atual
if ano == 0 :
    ano = date.today().year

# Saída
print("~ Resultado", '-'*38)
# Calcúlo de ano bissexto
if ano % 4 == 0 :
    if ano % 100 == 0 and ano % 400 != 0 :
        print(f"O ano {ano} NÃO pode ser BISSEXTO!")
    else :
        print("Ano BISSEXTO!")
else :
    print(f"O ano {ano} NÃO é bissexto!")

# Fim
print("\n-- FIM --")