"""
  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print("~ Números primos", '-'*33)
num = int(input("Informe um número: "))
# por MMC
c = 0
for n in range(num, 0, -1):
    if num % n == 0 :
        c += 1

print("~ Resultado", '-'*38)
if c == 2 :
    print(f"O número {num} \033[32mé PRIMO!\033[m")
else :
    print(f"O número {num} \033[31mNÃO\033[m é primo...")