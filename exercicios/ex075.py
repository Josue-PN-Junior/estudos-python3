"""
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
 A) Quantas vezes apareceu o valor 9.
 B) Em que posição foi digitado o primeiro valor 3.
 C) Quais foram os números pares.
"""
print("~ Análise de dados em uma Tupla", '-'*18)
# errado!
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2ª número: "))
# n3 = int(input("Digite o 3ª número: "))
# n4 = int(input("Digite 0 4ª número: "))
# numeros = (n1, n2 , n3 , n4)
numeros = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digete mais um número: ")),
           int(input("Digite mais outro número: ")))
print("~ Resultado", '-'*38)
print(f"@ Números: {numeros}")
print(f"> Ao todo temos {numeros.count(9)} valores nove digitados")
if 3 in numeros:
    print(f"> O primeiro valor 3 encontra está na {numeros.index(3)+1}ª posição ")
else :
    print("> Não há valor 3 na tupla...")
print(f"> Os números PARES digitados foram:", end=" ")
p = 0
for num in numeros :
    if num % 2 == 0 :
        print(num, end=" ")
        p = 1
if p == 0:
    print("Nenhum.")

