"""
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
 únicos digitados, em ordem crescente.
"""
print("~ Valores únicos em uma Lista", '-'*20)
numerosListados = list()
while True:
    num = int(input("Informe um valor: "))
    if num in numerosListados :
        print("# Valor já se encontra na lista... não adicionado novamente.")
    else :
        print("* Valor adicionado a lista!")
        numerosListados.append(num)

    # saída
    while True:
        resp = str(input("> Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        break
    print()
print("~ Resultado", '-'*38)
numerosListados.sort()
print(f"@ Valores informados: {numerosListados}")