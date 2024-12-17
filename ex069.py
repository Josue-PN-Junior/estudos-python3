"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
 se o usuário quer ou não continuar. No final, mostre:

 A) quantas pessoas tem mais de 18 anos.
 B) quantos homens foram cadastrados.
 C) quantas mulheres tem menos de 20 anos.
"""
cont = pessoas18 = homens = mulher20 = 0
print("~ Análise de dados do grupo", '-'*22)
while True:
    cont += 1
    print(f"\n{f" {cont}ª Pessoa ":-^50}")
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    # verifcação sexo
    while True :
        print("Opções sexo [M/F/O] : ")
        sexo = str(input("Sexo: ")).strip().upper()[0]
        if sexo in "OMF" :
            break
        else :
            print("** opção inválida...")

    if idade >= 18 :
        pessoas18 += 1

    if sexo == "M" :
        homens += 1

    if sexo == "F" and idade < 20:
        mulher20 += 1

    # continua?
    while True :
        resp = str(input("\nQuer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break

    # saída
    if resp == "N" :
        break

print("~ Resultado", '-'*38)
print(f"Pessoas cadastradas {cont}")
print(f"Pessoas com mais de 18 anos: {pessoas18}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulher20}")