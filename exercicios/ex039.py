"""
  Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime

# Início
print("~ Alistamento Militar", '-'*29)
sexo = str(input("Você é do sexo masculino? [S/N] ")).upper()

if sexo == 'S' :
    nasc = int(input("Qual é o seu ano de nascimento? "))

    # cálculo
    anoAtual =  datetime.now().date().year
    idade = anoAtual - nasc

    # codição e saída
    print("\n~ Resultado", '-'*39)
    print(f"> Ano atual {anoAtual}")
    if idade == 18 :
        print("Você DEVE se alistar ESSE ANO!")
    elif idade > 18 :
        print(f"Já se passaram {idade-18} ano(os) desde o alistamento!")
        print(f"Você se alistou em {anoAtual-(idade-18)}")
    else :
        print(f"Você deve se alistar em {18-idade} ano(os)!")
        print(f"Você deve se alistar em {anoAtual+(18-idade)}")
else :
    print("Você NÃO precisa se alistar!")