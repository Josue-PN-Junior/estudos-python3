"""
    Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
 valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
 elas (desconsiderando o flag).
"""
print("~ Vários números com flag", '-'*24)
soma = quantia = 0
while True:
    num = int(input("Digite um número: [999 para parar] "))
    if num == 999 :
        break
    soma += num
    quantia += 1
print("~ Resultado", '-'*38)
print(f"Formam informados {quantia} números e a soma deles é {soma}")