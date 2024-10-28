"""
  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
 o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
 ou então o empréstimo será negado.
"""

print("~ Aprovando Empréstimo", '-'*27) #23
val_casa = float(input("Qual é valor da casa? R$"))
salario = float(input("Informe seu salário: R$"))
anos = int(input("Em quantos anos pretende pagar? "))

# processamento
parcelas = anos * 12
val_parcelas = val_casa / parcelas


print("~ Resultado", '-'*38)
if val_parcelas <= salario*30/100 :
    print("Emprestimo \033[32mAPROVADO!\033[m")
    print(f"Serão \033[33m{parcelas}\033[m parcelas de R${val_parcelas:.2f}!")
else :
    print("Emprestimo \033[31mNEGADO!\033[m")