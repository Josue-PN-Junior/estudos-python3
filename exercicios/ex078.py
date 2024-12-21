"""
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e
 o menor valor digitado e as suas respectivas posições na lista.
"""
print("~ Maior e Menor valores na Lista", '-'*17)
listaNum = list()
for p in range(0, 5):
    listaNum.append(int(input(f"Digite um valor para a posição {p}: ")))
print("~ Resultado", '-'*38)
print(f"Valores digitados: ", end=" ")
for i in listaNum:
    print(f"{i}", end=' ')
# for maior
print(f"\nMaior valor encontrado: {max(listaNum)}, nas posições: ", end="")
for i, val in enumerate(listaNum):
    if val == max(listaNum):
        print(f"{i}", end=" ")
# for menor
print(f"\nMenor valor encontrado: {min(listaNum)}, nas posições: ", end="")
for i, val in enumerate(listaNum):
    if val == min(listaNum):
        print(f"{i}", end=" ")