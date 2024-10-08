"""
 Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

# entrada
print("~ Aluguel de Carros", "-"*27)
km = float(input("Quantos quilômetros foram rodados? "))
dias = int(input("Quantos dias alugados? "))

# processamento
valor_dias = dias * 60
valor_km = km * 0.15
valor = valor_km + valor_dias

# saída
print("~ Resultado", "-"*35)
print(f"O total a pagar é de R${valor:.2f}")