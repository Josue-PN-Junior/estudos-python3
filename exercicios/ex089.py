"""
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
 um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
print("~ Boletim com listas compostas", '-'*19)
listaAlunos = []
aluno = []
while True:
    print(f"{f" {len(listaAlunos)+1}º Aluno ":-^50}")
    nome = str(input("Nome: ")).strip().capitalize()
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    listaAlunos.append(aluno[:])
    aluno.clear()
    while True:
        resp = str(input("> Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        break

print("~ Resultado", '-'*38)
print("Alunos(as) e média:")
for i, al in enumerate(listaAlunos):
    media = 0
    print("- "*26)
    media = (al[1] + al[2]) / 2
    print(f"-- Cod: {i} | Aluno(a) {al[0]} média {media:2.1f}")
print("="*50)
while True:
    cod = int(input("> Quer mostras as notas de qual aluno? (para parar digite 999) Cod: "))
    if cod == 999 :
        break
    elif cod >= len(listaAlunos) or cod < 0:
        print("*** Aluno não encontrado!")
    else :
        media = 0
        print(f"\t- Aluno(a): {listaAlunos[cod][0]} ")
        print(f"\t- Primeira nota: {listaAlunos[cod][1]}")
        print(f"\t- Segunda nota: {listaAlunos[cod][2]}")
        media = (listaAlunos[cod][1] + listaAlunos[cod][2]) / 2
        print(f"\t- Média: {media:2.1f}")
    print("- " * 26)
print("{:=^50}".format(" Programa encerrado! "))