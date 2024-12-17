"""
  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print("~ Maior e menor da sequência", '-'*21)
for p in range(1,6):
    peso = float(input(f"Pessoa da {p}ª pessoa: (kg) "))
    if p == 1 :
        maiorPeso = peso
        menorPeso = peso
    else :
        if peso > maiorPeso :
            maiorPeso = peso
        elif peso < menorPeso :
            menorPeso = peso

print("~ Resultado", '-'*38)
print(f"O maior peso lido foi {maiorPeso}Kg, e menor peso foi {menorPeso}Kg!")