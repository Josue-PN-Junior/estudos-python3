"""
  Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
 mostre os 10 primeiros termos dessa progressão.
"""
print("~ Progressão Aritmética", '-'*26)
n1 = int(input("Primeiro termo da progreção aritmética: "))
r = int(input("Razão da progressão: "))

print("~ Resultado", '-'*38)
print("PA: ", end='')
for pa in range(1, 11):
    n = n1 + (pa - 1) * r
    print(n, end=' ')


print("\n\n- Guanabra")
dec = n1 + (10 - 1) * r
print("PA:", end=" ")
for i in range(n1, dec + r, r):
    print(i, end=" ")