# Mostrar Dobro, Triplo, Raiz Quadrada de um número
from jinja2.filters import do_random

#entrada
print("~ Dobro, Triplo, Raiz Quadrada", "-"*6)
num = int(input("Digite um número: "))

#calculos
dobro = num * 2
tr = num * 3
rz = num ** (1/2)
#saída
print("~ Resultado", "-"*25)
print(f"O dobro de {num} vale {dobro}\n"
      f"O triplo de {num} vale {tr}\n"
      f"A raiz quadrada de {num} é igual a {rz:.2f}")