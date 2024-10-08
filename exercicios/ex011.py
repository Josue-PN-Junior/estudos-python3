# Calcule a área de uma parede e a tinta necessária para pinta-lá

# entrada
print("~ Pintando Parede", "-"*10)
larg = float(input("Largura da parede em metros: "))
alt = float(input("Altura da parede em metros: "))

# processamento
metros_qd = larg * alt
tinta = metros_qd / 2

#saída
print("~ Resultado", "-"*16)
print(f"A parede tem a dimensão de {larg:.2f}x{alt:.2f} e sua área é de {metros_qd}m².")
print(f"Para pintar essa parede, você precisará de {tinta:.3f}l de tinta.")