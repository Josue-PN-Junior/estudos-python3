"""
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
 separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
print("~ Listas com pares e ímpares", '-'*  31)
# listaNum = []
# listaPar = []
# listaImpar = []
# for n in range(1, 8):
#     num = int(input(f"Informe o {n}º valor: "))
#     if num % 2 == 0:
#         listaPar.append(num)
#     else :
#         listaImpar.append(num)
# listaPar.sort()
# listaImpar.sort()
# listaNum.append(listaPar)
# listaNum.append

# funciona
listaNum = [[], []]
for i in range(1, 8):
    num = int(input(f"Informe o {i}º valor: "))
    if num % 2 == 0:
        listaNum[0].append(num)
    else :
        listaNum[1].append(num)
listaNum[1].sort()
listaNum[0].sort()
print("~ Resultado", '-'*38)
print(f"Dados: {listaNum}")
print(f"Valores PARES: {listaNum[0]}")
print(f"Valores IMPARES: {listaNum[1]}")