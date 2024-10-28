"""
 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

print("~ Maior e menor valores", '-'*26) #23
# entrada das variáveis
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# verificador de número maior
if num1 > num2 :
    maior = num1
    menor = num2
    if num3 < menor :
        menor = num3
    if num3 > maior :
        maior = num3
else :
    maior = num2
    menor = num1
    if num1 > num3 :
        menor = num3
    if num3 > num2 :
        maior = num3

# saída de resultado
print("~ Resultado", '-'*38)
print(f"Maior número informado: {maior}")
print(f"Menor número informado: {menor}")
