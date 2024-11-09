"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""
# Início
print("~ Comparando números", '-'*29) #21
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

# comparações e saída
print("~ Resultado", '-'*38)
if num1 > num2 :
    print("> O PRIMEIRO número é maior que o segundo número!")
elif num1 < num2 :
    print("> O SEGUNDO número é maior que o primeiro número!")
else :
    print("> Os DOIS números são iguais, logo não há um maior!")