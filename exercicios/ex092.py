"""
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
 acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime
func = {}
anoAtual = datetime.today().year
print(f"** Ano atual {anoAtual}")
print("~ Cadastro de Trabalhador em Python", '-'*14)
nomeFunc = str(input("Nome funcionário(a): ")).strip().capitalize()
anoNasc = int(input("Ano de nascimento: "))
ctps = int(input("Número carteira de trabalho ( 0 se não houver): "))
func['nomeFunc'] = nomeFunc
func['idade'] = (anoAtual - anoNasc)
func['ctps'] = (ctps)
if ctps != 0:
    anoContratação = int(input("Ano de contratação: "))
    sal = float(input("Salário: R$"))
    func['anoCont'] = anoContratação
    func['sal'] = sal
    # aposentadoria
    anoAposenta = anoContratação + 55
    func['apose'] = anoAposenta
print("~ Resultado", '-'*38)
print(f" @ Nome: {func['nomeFunc']}")
print(f" # Idade: {func['idade']} anos")
if func['ctps'] != 0:
    print(f" & CTPS: {func['ctps']}")
    print(f" = Ano de contratação: {func['anoCont']}")
    print(f" $ Salário: R${func['sal']:.2f}")
    print(f" % Idade de aposentadoria: {func['apose']-anoNasc} anos")
else :
    print(" * Não possue CTPS")