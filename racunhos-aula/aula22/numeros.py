from uteis import numeros
ut = numeros

# Programa Principal
num = int(input("Digite um número: "))
fat = ut.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {ut.dobro(num)}.")
print(f"O triplo de {num} é {ut.triplo(num)}.")