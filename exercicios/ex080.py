"""
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
print("~ Lista ordenada sem repetições", '-'*18)
listaNumerica = list()
for i in range(0, 5):
    num = int(input("Insira um número: "))
    if i == 0 or num > max(listaNumerica):
        listaNumerica.append(num)
        print("Número adicionado ao final da lista!")
    else :
        for valor in range(0, len(listaNumerica),1) :
            if num <= listaNumerica[valor]:
                listaNumerica.insert(valor, num)
                print(f"Valor adicionado na posição {valor}")
                break


print("~ Resultado", '-'*38)
print(f"Os números informados foram: {listaNumerica}")
