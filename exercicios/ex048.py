"""
  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
 que se encontram no intervalo de 1 até 500.
"""
print("~ Soma ímpares múltiplos de três", '-'*17)
soma = 0 # zerar var
for num in range(3, 501, 3) :
    soma += num

print(f"A soma é {soma}")

soma = 0 # zerar
print("\n~ Soma impares", '-'*35)
for num in range(1, 501, 2) :
    if num % 3 == 0 :
        soma += num
print(f"A soma dos números impáres multiplos de 3: {soma}")

soma = 0 # zerar
# otmizado
for num in range(3, 501, 6):
    soma += num
print(f"A soma dos números impáres multiplos de 3: {soma}")