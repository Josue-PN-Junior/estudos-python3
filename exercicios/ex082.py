"""
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
 conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
 listas geradas.
"""
print("~ Dividindo valores em várias listas", '-'*13)
# as lista não podem estar linkadas se não elas se alimenta pra sempre !!! e no for fica infinito
listaNumGerais = list()
listaPares = list()
listasImpares = list()
while True:
    listaNumGerais.append(int(input("Digite um valor: ")))
    while True:
        resp = str(input("> Quer continuar? ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp in "N":
        break
print("~ Resultado", '-'*38)
print(f"Lista Digitada: {listaNumGerais}")
for num in listaNumGerais:
    if num % 2 == 0:
        listaPares.append(num)
    else :
        listasImpares.append(num)
if len(listasImpares) == 0 :
    print("Não há números impares!")
else :
    print(f"Valores Impares: {listasImpares}")

if len(listaPares) == 0:
    print("Não foi informados números pares!")
else :
    print(f"Valores Pares: {listaPares}")