"""
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
 continuar ou não. No final, mostre:
 A) qual é o total gasto na compra.
 B) quantos produtos custam mais de R$1000.
 C) qual é o nome do produto mais barato.
"""
qtProd = totalValor = prodMais = 0
print("~ Estatísticas em produtos", '-'*23)
while True:
    qtProd += 1
    print(f"\n{f" {qtProd}ª Produto ":-^50}")
    nomeProd = str(input("Nome do produto: "))
    valorProd = float(input("Valor do produto: R$"))
    totalValor += valorProd
    if valorProd > 1000 :
        prodMais += 1
    if qtProd == 1 :
        nomeMenorProd = nomeProd
        valorMenorProd = valorProd
    elif valorProd < valorMenorProd:
        nomeMenorProd = nomeProd
        valorMenorProd = valorProd

    # saída
    while True:
        resp = str(input("\n> Quer continuar? ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N" :
        break

print("~ Resultado", '-'*38)
print(f"Gasto total R${totalValor:.2f}")
print(f"Foram registrados {prodMais} produtos acima de R$1000")
print(f"O produto mais barato foi {nomeMenorProd} custando R${valorMenorProd:.2f}")