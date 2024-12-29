"""
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
 a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
 processo de cálculo do fatorial.
"""
def fatorial(num=1, show=False) :
    """
    Faz o cálculo do fatorial de um número!
    :param num: recebe o número que vai ser feito o fatorial
    :param show: (opcional) recebe verdadeiro ou falso para mostrar o processo
    :return: retorna o fatorial do número
    """
    f = 1
    if show:
        print('F: ', end='')
        for n in range(num, 0, -1):
            f *= n
            if n == 1:
                print(n)
            else :
                print(n, end=' x ')
    else :
        for n in range(num, 0, -1):
            f *= n

    return f


# __ Programa Principal __
print("~ Função para Fatorial", '-'*27)
num = int(input("Informe um número: "))
res = str(input("Visualizar? [S/N] ")).strip().upper()[0]
print("~ Resultado", '-'*38)
if res in "S":
    fat = fatorial(num, show=True)
else:
    fat = fatorial(num)
print(f"O fatorial de {num} é {fat}!")

print("\n\n")
print(f"Função sem passar parâmetros F:{fatorial(show=True)} fatorial de 1 ")
help(fatorial)