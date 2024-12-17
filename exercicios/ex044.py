"""
  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

 – à vista dinheiro/cheque: 10% de desconto

 – à vista no cartão: 5% de desconto

 – em até 2x no cartão: preço formal

 – 3x ou mais no cartão: 20% de juros
"""

print("~ Gerenciador de Pagamentos", '-'*22)
valor = float(input("Valor do produto: R$"))
print("- "*25)
print("- Opções de pagamento : ")
print("- [ 1 ] À vista dinheiro/pix:\033[32m 10% de desconto\033[m")
print("- [ 2 ] À vista no cartão:\033[32m 5% de desconto\033[m")
print("- [ 3 ] Parcelado em 2x no cartão:\033[34m Preço Normal\033[m")
print("- [ 4 ] Parcelado em 3x ou mais:\033[31m 20% de juros\033[m")
tipoPag = int(input("- SELECIONE A FORMA DE PAGAMENTO: "))
print("\n@ Forma de pagamento: ", end="")
if tipoPag == 1 :
    print("À vista em dinheiro ou pix.")
    desconto = 10/100
elif tipoPag == 2 :
    print("À vista cartão.")
    desconto = 5/100
elif tipoPag == 3 :
    print("Parcelado em 2x no cartão.")
    desconto = 0
    juros = 0.0
elif tipoPag == 4 :
    print("Parcelado em 3x ou mais no cartão.")
    desconto = 0
    juros = (20/100)
else :
    print("\033[31mTipo de pagamento inválido!\033[m")
    desconto = 0
    juros = 0.0

# cálculo
if desconto == 0 :
    if juros != 0.0 :
        valorFinal = valor + juros * valor
        parcelado = int(input("> Parcelar em quantas vezes? "))
        print(f"* Parcelado em {parcelado}x de R${valorFinal/parcelado:.2f}")
        print(f"* Valor final do produto com juros de 20% R${valorFinal}")
    else :
        print(f"* Parcelado em 2x de R${valor/2:.2f}")
        print(f"* Valor final do produdo R${valor:.2f}")
else :
    valorFinal = valor - ( valor * desconto )
    print(f"* Valor final do produto com desconto de {desconto*100:.0f}%: R${valorFinal:.2f}")
