"""
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

def leiaInt(msg=""):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            break
        print("\033[31m**ERRO, Informe um número inteiro...\033[m")
    return int(num)


# __ Programa Principal __
print("~ Validando entrada de dados em Python", '-'*11)
n = leiaInt("Digite um número: ")
print("~ Resultado", '-'*38)
print(f"O valor informado é válido! Número {n}")
# p = leiaInt()