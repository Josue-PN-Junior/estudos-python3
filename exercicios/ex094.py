"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas
 B) A média de idade
 C) Uma lista com as mulheres
 D) Uma lista de pessoas com idade acima da média
"""
print("~ Unindo dicionários e listas", '-'*20)
pessoa = {}
grupo = []
while True:
    pessoa['nome'] = str(input("Nome: ")).strip().capitalize()
    while True:
        sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
        if sexo in "MF":
            break
        else :
            print("**Opção inválida...")
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input("Idade: "))
    grupo.append(pessoa.copy())

    print("- "*26)
    while True:
        resp = str(input("> Quer continuar a adicionar pessoas? ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        break
print("\n~ Resultado", '-'*38)
print(f"- Pessoas cadastradas: {len(grupo)}")
somaIdade = media = qtM = 0
for p, d in enumerate(grupo):
    somaIdade += d['idade']
media = somaIdade / len(grupo)
print(f"- Média de idade do grupo {int(media)} anos")
print(f"- Mulheres cadastradas: ")
for dic in grupo:
    if dic["sexo"] == 'F':
        print(f"\t- {dic['nome']}")
        qtM += 1
if qtM == 0:
    print("\033[31mNão foram cadastradas mulheres\033[m")
print(f"- Pessoas com mais de {int(media)} anos: ")
for dic in grupo:
    if dic['idade'] > int(media):
        print(f"\t- {dic['nome']}")
