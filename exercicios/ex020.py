"""
  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
 trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
 e mostre a ordem sorteada.
"""
from random import shuffle

# entrada
print("~ Sorteando uma ordem na lista", "-"*20) #30+20 = 50 R12
al1 = input("Primeiro Aluno: ")
al2 = input("Segundo Aluno: ")
al3 = input("Terceiro Aluno: ")
al4 = input("Quarto Aluno: ")

# sorteio e processamento
lista = [al1, al2, al3, al4]
# embaralha internamente
shuffle(lista)
sort = lista

# saída
print("~ Resultado", "-"*38)
print(sort)