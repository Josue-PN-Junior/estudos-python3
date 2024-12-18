"""
  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
 um atleta e mostre sua categoria, de acordo com a idade:

 – Até 9 anos: MIRIM

 – Até 14 anos: INFANTIL

 – Até 19 anos: JÚNIOR

 – Até 25 anos: SÊNIOR

 – Acima de 25 anos: MASTER
"""
import datetime

print("~ Classificando Atletas",'-'*26)
anoNasc = int(input("Ano de nascimento: "))
# processamento
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasc
# saída
print("~ Resultado", '-'*38)
print(f"** Ano atual: {anoAtual}")
# condições
print("=== CATEGORIA: ")
if idade <= 9 :
    print("> MIRIM")
elif idade <= 14 :
    print("> INFANTIL")
elif idade <= 19 :
    print("> JÚNIOR")
elif idade <= 25 :
    print("> SÊNIOR")
elif idade > 25 :
    print("> MASTER")