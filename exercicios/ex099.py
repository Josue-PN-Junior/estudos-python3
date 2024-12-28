"""
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
def maior(num) :
    maiorN = 0
    for i, n in enumerate(num):
        if i == 0 or n > maiorN:
            maiorN = n
    print(f"* O maior número informado foi: {maiorN}")
    print(f"- Ao todo foram informados {len(num)} números")

def maiorNum(*numeros):
    numMaior = 0
    print('-'*50)
    print("Valores informados: ", end="")
    for i, v in enumerate(numeros):
        print(v, end=' ')
        if i == 0 or v > numMaior:
            numMaior = v
    print(f"\n- Ao todo foram informados {len(numeros)} números")
    print(f"* Maior valor informado: {numMaior}")



# __ Programa Principal __
print("~ Função que descobre o maior", '-'*20)

valores = list()
cont = 0
while True:
    cont += 1
    valores.append(int(input(f"Informe o {cont}º valor: ")))

    while True:
        resp = str(input("> Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break

    if resp == "N":
        break

print("~ Resultado", '-'*38)
print(f"Valores informados: {valores}")
maior(valores)

print("\n\nMétodo 2")
maiorNum(1, 2)
maiorNum(1)
maiorNum(3, 1 , 3)
maior()