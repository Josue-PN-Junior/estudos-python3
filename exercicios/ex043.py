"""
  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

 – IMC abaixo de 18,5: Abaixo do Peso

 – Entre 18,5 e 25: Peso Ideal

 – 25 até 30: Sobrepeso

 – 30 até 40: Obesidade

 – Acima de 40: Obesidade Mórbida
"""

from math import pow

print("~ Índice de Massa Corporal", '-'*23)
altura = float(input("Qual é sua altura? "))
peso = float(input("Qual é o seu peso? Kg "))
# cálculo de IMC
imc = peso / pow(altura, 2)
print("~ Resultado", '-'*38)
print(f"IMC: {imc:.1f}")
# possibilidades
if imc <= 18.5 :
    print("Abaixo do peso!")
elif imc <= 25 :
    print("Peso Ideal!")
elif imc <= 30 :
    print("Sobre peso!")
elif imc <= 40 :
    print("Obesidade!")
elif imc >= 40 :
    print("Obesidade Mórbida!")
