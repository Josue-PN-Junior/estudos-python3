"""
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
 mostre o conteúdo da estrutura na tela.
"""
print("~ Dicionário em Python", '-'*27)
aluno = {}
nome = str(input("Qual é o nome do aluno(a): ")).strip().capitalize()
media = float(input("Média do aluno(a): "))
aluno['nome'] = nome
aluno['media'] = media
if media >= 6:
    aluno['situacao'] = "\033[32mAPROVADO\033[m"
elif media >=4 :
    aluno['situacao'] = "\033[33mRECUPERÇÃO\033[m"
elif media < 4 :
    aluno['situacao'] = "\033[31mREPROVADO\033[m"
print("~ Resultado", '-'*38)
print(f"Nome: {aluno['nome']}")
print(f"Média: {aluno['media']}")
print(f"Situação: {aluno['situacao']}")