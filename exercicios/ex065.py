"""
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
 valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
print("~ Maior e Menor valores", '-'*26)
soma = cont = 0
resp = "S"
while resp[0] == "S":
    num = int(input("Informe um número: "))
    soma += num
    cont += 1

    if cont == 1 :
        maiorNum = menorNum = num
    else :
        if num > maiorNum :
            maiorNum = num
        elif num < menorNum :
            menorNum = num

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
print("~ Resultado", '-'*38)
print(f"Foram informados {cont} números"
      f"\nSoma dos números: {soma}"
      f"\nMédia entre os números: {soma/cont}"
      f"\nMaior valor informado: {maiorNum}"
      f"\nMenor valor informado: {menorNum}")