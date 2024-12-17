"""
  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
 mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
from operator import is_not

idadeSoma = 0
idadeHMV = 0
mulher20 = 0

print("~ Analisador completo", '-'*28)
for p in range(1, 5):
    nome: str = str(input(f"Nome da {p}ª pessoa: ")).capitalize().strip()
    idade = int(input("Idade: "))
    idadeSoma += idade
    print("- Sexo Opções :")
    print("""[ 1 ] Mulher
[ 2 ] Homem
[ 3 ] Outro""")
    sexo = int(input("Escolha: "))
    print('-'*50)
    if sexo == 2 :
        if idade > idadeHMV :
            nomeHMV = nome
            idadeHMV = idade
    elif sexo == 1 :
        if idade < 20 :
            mulher20 += 1



print("~ Resultado", '-'*38)
print(f"A média de idade do grupo é de {idadeSoma/4:.0f} anos")
if idadeHMV == 0:
    print("Não foram informados homens...")
else :
    print(f"O homem mais velhor é {nomeHMV} com {idadeHMV} anos")
print(f"A {mulher20} mulheres com menos de 20 anos")
