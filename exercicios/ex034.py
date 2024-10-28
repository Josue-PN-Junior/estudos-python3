"""
  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.
"""

print("~ Aumentos múltiplos", '-'*29) #21
sal = float(input("Qual é o seu salário atual? R$"))

# condições
if sal > 1250.00 :
    valorAumento = "10%"
    porcent = 1/10
else :
    valorAumento = "15%"
    porcent = 15/100

# processamento
aumento = sal * porcent
novoSal = sal + aumento

# saída
print("~ Resultado", '-'*38)
print("Aumento de", valorAumento, f"(R${aumento:.2f})")
print(f"Seu novo salário é de R${novoSal:.2f}")
