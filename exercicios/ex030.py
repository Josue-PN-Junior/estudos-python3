"""
  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

# Início
print("~ Par ou Ímpar?", '-'*34) #16
num = int(input("Informe um número inteiro: ")) # recebe o número a ser testado

# processamento e saída de resultado
print("~ Resultado", '-'*38)

# condições
if num % 2 == 0 :
    # par
    print(f"\n\tO número {num} é PAR !")
else :
    #impar
    print(f"\n\tO número {num} é IMPAR !")

# Fim
print("\n-- FIM --")
