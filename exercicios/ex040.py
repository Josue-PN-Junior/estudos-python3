"""
  Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
 de acordo com a média atingida:

 – Média abaixo de 5.0: REPROVADO

 – Média entre 5.0 e 6.9: RECUPERAÇÃO

 – Média 7.0 ou superior: APROVADO
"""

cor = {
    "amr" : "\033[33m",
    "vrm" : "\033[31m",
    "vrd" : "\033[32m",
    "azl" : "\033[34m",
    "f"   : "\033[m"
}

# Início
print("~ Aquele clássico da Média", '-'*23) #27
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

# média
media = (nota1 + nota2) / 2

# saída e condições
print("\n~ Resultado", '-'*38)
print(f"> Média do aluno(a): {cor["azl"]}{media:.1f}{cor["f"]}")

if media < 5.0 and media >= 0 :
    print(f"\nMédia abaixo de 5.0: {cor["vrm"]}REPROVADO{cor["f"]}")
elif media >= 5.0 and media < 7 :
    print(f"\nMédia entre 5.0 e 6.9: {cor["amr"]}RECUPERAÇÃO{cor["f"]}")
elif media >= 7 and media <= 10 :
    print(f"\nMédia entre 7 e 10: {cor["vrd"]}APROVADO{cor["f"]}")
else :
    print(f"Média \033[4;41;30m INVÁLIDA \033[m!")