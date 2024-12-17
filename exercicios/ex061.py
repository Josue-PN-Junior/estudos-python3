"""
  Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
 os 10 primeiros termos da progressão usando a estrutura while.
"""
print("~ Progressão Aritmética v2.0", '-'*21)
n1 = int(input("Informe um número: "))
r = int(input("Iforme a razão: "))
n = 1
print("~ Resultado", '-'*38)
print("PA: ", end="")
while n <= 10 :
    pa = n1 + (n - 1) * r
    n += 1
    print(pa, end=" ")

