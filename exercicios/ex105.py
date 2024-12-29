"""
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
 com as seguintes informações:
 – Quantidade de notas
 – A maior nota
 – A menor nota
 – A média da turma
 – A situação (opcional)
"""


# poderia ser empacortamento...
def notas(listaNota, sit=False):
    """
    -> Recebe uma lista de notas
    :param listaNota: lista com várias notas
    :param sit: (opcional) mostra a siatuação com base na média das notas
    :return: retorna um dicionário com as quantidade de notas, maior e menor nota e a média
    """
    notasTot = alunos = 0
    for i, n in enumerate(listaNota):
        notasTot += n
        alunos += 1
        if i == 0:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
    media = notasTot / alunos
    dic = {
        "notas": alunos,
        "menor": menor,
        "maior": maior,
        "media": media
    }
    if sit:
        if media <= 2:
            mediaSit = "\033[31mEXTREMAMENTE RUIM\033[m"
        elif media <= 3:
            mediaSit = "\033[31mMUITO RUIM\033[m"
        elif media <= 5:
            mediaSit = "\033[35mRUIM\033[m"
        elif media <= 7:
            mediaSit = "\033[33mBOA\033[m"
        elif media < 9:
            mediaSit = "\033[36mÓtima\033[m"
        elif media >= 9:
            mediaSit = "\033[32mMUITO BOM\033[m"
        else :
            mediaSit = "ERRO"
        dic['situacao'] = mediaSit
    return dic




# __ Programa Principal __
print("~ Analisando e gerando Dicionários", '-'*15)
aluno = 0
totNotas = list()
while True:
    aluno += 1
    print(f"{f" {aluno}º Aluno(a) ":-^50}")
    nota = float(input("Adicionar nota: "))
    totNotas.append(nota)

    while True:
        resp = str(input("> Quer continuar a adicionar notas? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
        print("**somente S ou N...")
    if resp == "N":
        while True:
            situacao = str(input("> Quer ver a situação da turma? [S/N] ")).strip().upper()[0]
            if situacao in "SN":
                break
        if situacao == "S":
            sitR = True
        else :
            sitR = False
        break
print("\n~ Resultado", '-'*38)
dicNota = notas(totNotas, sitR)
print(dicNota)
print(f"Notas: {dicNota['notas']}")
print(f"Menor nota: {dicNota['menor']}")
print(f"Maior nota: {dicNota['maior']}")
print(f"Média notas: {dicNota['media']:.1f}")
if sitR:
    print(f"Situação: {dicNota['situacao']}")
