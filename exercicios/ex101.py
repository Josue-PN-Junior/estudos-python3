"""
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
 pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
from datetime import datetime


def voto(nasc = datetime.now().year):
    ano = datetime.now().year
    idade = ano - nasc
    if idade <= 0:
        return 0
    elif idade < 16:
        return 1
    elif 18 > idade >= 16 or idade >= 65:
        return 2
    else :
        return 3


# __ Programa Principal __
votos = {
    0 : "\033[31m**INVÁLIDO\033[m",
    1 : "\033[31mNÃO é permitido\033[m",
    2 : "é \033[33mopcional\033[m",
    3 : "é \033[32mobrigatorio\033[m"
}


print("~ Funções para votação", '-'*27)
anoNasc = int(input("Qual é o seu ano de nascimento? "))
anoAtual = datetime.now().year
print(f"Ano atual: {anoAtual}")
print("~ Resultado", '-'*38)
v = voto(anoNasc)
print(f"* Com {anoAtual-anoNasc} anos de idade, o voto {votos[v]}")
