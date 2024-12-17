"""
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
 digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
 a soma entre eles (desconsiderando o flag).
"""
print("~ Tratando vários valores v1.0", '-'*19)
soma = cont = 0
num = int(input("Digite um número: "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite outro número: "))
    if num != 999:
        print("* digite 999 para parar...")
print("~ Resultado", '-'*38)
print(f"Foram digitados {cont} números, a soma deles é {soma}")