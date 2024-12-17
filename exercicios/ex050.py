"""
  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o.
"""
print("~ Soma dos pares", '-'*33)
soma = 0
for n in range(6) :
    num = int(input(f"Informe o {n+1}º número: "))
    if num % 2 == 0 :
        soma += num

print("~ Resultado", '-'*38)
print(f"A soma do valores é {soma}")
