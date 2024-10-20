"""
  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

# Início
print("~ Custo da Viagem", '-'*32) #18
kms = float(input("Quantos quilômetros de viagem? Km ")) # entrada da distância percorrida

# processamento
if kms <= 200 :
    # menos de 200km
    valor_km = 0.50
else :
    # mais de 200km
    valor_km = 0.45

valor = kms * valor_km # valor final a ser pago
# valor = kms * 0.50 if kms <= 200 else kms * 0.45 # if simplificado

# saída
print("~ Resultado", '-'*38)
print(f"\nValor por km R${valor_km:.2f}, distância {kms}Km")
print(f"Valor da passagem R${valor:.2f}")

# Fim
print("\n-- FIM --")
