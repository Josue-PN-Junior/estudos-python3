"""
  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

print("~ Validação de Dados", '-'*29)
nome = str(input("Qual é o seu nome? ")).strip()
# opção 1
# sexo = ''
# while  sexo != "F" and sexo != "M" :
#     sexo = str(input("Qual seu é sexo: [F/M] ")).upper()

# opção 2
res = False
while not res:
    sexo = str(input("Qual é seu sexo: [F/M] ")).strip().upper()
    if sexo != "F" and sexo != "M" :
        res = False
        print("\033[31mOpção inválida! \033[m")
    else :
        res = True
print("\n~ Resultado", '-'*38)
print(f"Nome: {nome}")
if sexo == "M" :
    print(f"Sexo: Masculino")
else :
    print("Sexo: Feminino")