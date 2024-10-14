"""
  Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos dígitos separados.
"""

print("~ Separando dígitos de um número", "-"*17) #33 R12
digito = str(input("Digte um número de 0 a 9999: ")).strip()   # entrada do digito

#processamento

# metodo gambiarra
nums = ["0", digito, "000"]
#print(nums)
digito = ''.join(nums)
#print(digito)
qt_dig = len(digito)

# metodo matemático
n = int(digito)
u = n // 1 % 10 # unidade
d = n // 10 % 10 # dezena
c = n // 100 % 10 # centena
m = n // 1000 % 10 # milhar
# basta mostrar eles

#saída
print("~ Resultado", "-"*38)
print(f"Unidade: {digito[qt_dig-4]}")
print(f"Dezena: {digito[qt_dig-5]}")
print(f"Centena: {digito[qt_dig-6]}")
print(f"Milhar: {digito[qt_dig-7]}")

