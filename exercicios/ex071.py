"""
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
 o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
 considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
nota50 = nota20 = nota10 = nota1 = 0
print("~ Simulador de Caixa Eletrônico", '-'*18)
print("$",'-'*46, "$")
print(f"{" CAIXA ELETRÔNICO ":^50}")
print("$", "-"*46, '$')
valor = int(input("> Qual valor deseja sacar? R$"))
saque = valor

while True:
    if saque <= 0:
        break
    if saque % 50 == 0 :
        saque -= 50
        nota50 += 1
    elif saque % 20 == 0 :
        saque -= 20
        nota20 += 1
    elif saque % 10 == 0 :
        saque -= 10
        nota10 += 1
    elif saque % 1 == 0 :
        saque -= 1
        nota1 += 1


print("~ Resultado", '-'*38)
print(f"Saída: ")
if nota50 >= 1:
    print(f"{nota50} notas de R$50")
if nota20 >= 1:
    print(f"{nota20} notas de R$20")
if nota10 >= 1:
    print(f"{nota10} notas de R$10")
if nota1 >= 1:
    print(f"{nota1} notas de R$1")
if valor <= 0 :
    print(f"** valor inválido...")

print("\n\nMais precisso!")
nota50 = nota20 = nota10 = nota1 = 0
saque = valor
while True:
    if saque <= 0:
        break
    if saque - 50 >= 0 :
        saque -= 50
        nota50 += 1
    elif saque - 20 >= 0 :
        saque -= 20
        nota20 += 1
    elif saque - 10 >= 0 :
        saque -= 10
        nota10 += 1
    elif saque - 1 >= 0 :
        saque -= 1
        nota1 += 1

print("~ Resultado", '-'*38)
print(f"Saída: ")
if nota50 >= 1:
    print(f"{nota50} notas de R$50")
if nota20 >= 1:
    print(f"{nota20} notas de R$20")
if nota10 >= 1:
    print(f"{nota10} notas de R$10")
if nota1 >= 1:
    print(f"{nota1} notas de R$1")
if valor <= 0 :
    print(f"** valor inválido...")