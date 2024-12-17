"""
    Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
 uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print("~ Sequência de Fibonacci v1.0", '-'*20)
n = int(input("Digite um número: "))
c = 0
f1 = 1
f = 0
print("~ Resultado", '-'*38, "\nFI: ", end="")
while c < n :
    # print em cima mostra o zero
    # print em baixo não mostra o zero
    print(f, end=" ")
    f2 = f1
    f1 = f
    f = f1 + f2
    c += 1