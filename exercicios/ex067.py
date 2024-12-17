"""
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.
"""
print("~ Tabuada v3.0", '-'*35)
while True:
    num = int(input("Quer saber a tabuada de qual número? "))
    if num < 0 :
        break
    print('-'*50)
    print(f"{f"T A B U A D A - DO - {num}":^50}")
    print('-'*50)
    for c in range(11) :
        print(f"{c:2} X {num} = {num*c}")
    print('-'*50)
    print("** informe um número negativo para parar...", end="\n\n")

print("Fim")