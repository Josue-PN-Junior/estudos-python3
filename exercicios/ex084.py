"""
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""
print("~ Lista composta e análise de dados", '-'*14)
pessoa = list()
grupoPessoas = []
pessoasLeves = []
pessoasPesadas = []
while True:
    nome = str(input("Nome: ")).strip().capitalize()
    peso = float(input("Peso: kg "))
    pessoa.append(nome)
    pessoa.append(peso)
    grupoPessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        resp = str(input("> Deseja adicionar mais pessoas? [S/N] ")).strip().upper()[0]
        if resp in "NS":
            break
    if resp == 'N':
        break
    print("- "*26)
print("~ Resultado", '-'*38)
print(f"@ Foram informadas {len(grupoPessoas)} pessoas para cadastro!")
print(f"^ Pessoas pesadas: (mais de 100kg)")
for i, p in enumerate(grupoPessoas):
    if p[1] > 100.0:
        print("\t-", f"{p[0]} com {p[1]}Kg")
print(f"¬ Pessoas leves: (menos de 60kg) ")
for p in grupoPessoas:
    if p[1] < 60:
        print(f"\t- {p[0]} com {p[1]}Kg")
for i, p in enumerate(grupoPessoas):
    if i == 0 :
        pessoasLeves.append(p)
    elif p[1] == pessoasLeves[0][1]:
        pessoasLeves.append(p)
    elif p[1] < pessoasLeves[0][1] :
        pessoasLeves.clear()
        pessoasLeves.append(p)
    if i == 0 :
        pessoasPesadas.append(p)
    elif p[1] == pessoasPesadas[0][1] :
        pessoasPesadas.append(p)
    elif p[1] > pessoasPesadas[0][1] :
        pessoasPesadas.clear()
        pessoasPesadas.append(p)
print(f"- Pessoas mais leves: ")
for pes in pessoasLeves:
    print(f"\t- {pes[0]} com {pes[1]}Kg")
print(f"+ Pessoas mais pesadas:")
for pes in pessoasPesadas:
    print(f"\t- {pes[0]} com {pes[1]}Kg")

