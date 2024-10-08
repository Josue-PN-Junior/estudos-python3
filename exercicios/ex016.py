#  Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

# entrada
print("~ Quebrando um número", "-"*30) #+23=53
num = float(input("Digite um número Real: "))

# processamento
num_int = trunc(num)

# saída
print("~ Resultado", "-"*40) #+13
print(f"O número {num} tem a parte inteira {num_int}.")
# print(f"O número {num} tem a parte inteira {int(num)}.")
