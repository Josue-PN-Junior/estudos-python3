"""
  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random

# entrada
print("~ Sorteando um item na lista", "-"*21) # 29+31 = 50 R12
aluno1 = input("Primeiro(a) aluno(a): ")
aluno2 = input("Segundo(a) aluno(a): ")
aluno3 = input("Terceiro(a) aluno(a): ")
aluno4 = input("Quarto(a) aluno(a): ")

# sorteio
sor = random.choice([aluno1, aluno2, aluno3, aluno4])
# tem que criar lista temporaria

# saída
print("~ Resultado", "-"*38)
print(f"O(a) aluno(a) sorteado(a) foi o(a) {sor}!")