"""
  Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import datetime
print("~ Grupo da Maioridade", '-'*28)
anoAtual = datetime.today().year
pesMaior = 0
pesMenor = 0
for p in range(1, 8) :
    print(f"{p}ª Pessoa:")
    anoNasc = int(input("Qual é o ano de nascimento? "))
    if anoAtual - anoNasc >= 18 :
        pesMaior += 1
    else :
        pesMenor += 1
    print('-'*50)

print("~ Resultado", '-'*38)
print(f"* {pesMaior} pessoas atingiram a MAIORIDADE! ")
print(f"* {pesMenor} pessoas NÃO atingiram maioridade...")