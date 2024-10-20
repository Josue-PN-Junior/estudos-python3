"""
  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
 que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

# Início
print("~ Radar eletrônico", '-'*31) #19
vel = float(input("Velocidade do carro: Km/h ")) # entrada da velocidade

# processamento e saída
print("~ Resultado", '-'*38)

# condições
if vel > 80 :
    print(f"\n!!! ACIMA da velocidade permitida !!! \n\t* {vel-80} Km/h acima do permitido (80Km/h) !!!")
    # calculo da multa
    multa = (vel - 80) * 7.00
    print(f"\tMULTADO! Valor da multa R${multa:.2f}")
else :
    print("\nDentro do limite de velocidade!")

# fim
print("\n-- FIM --")
