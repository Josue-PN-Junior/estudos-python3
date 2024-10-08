# calculo de desconto de 5%
from time import perf_counter

# entrada
print("~ Calculando Descontos", "-"*10)
valor = float(input("Valor da compra: R$"))

#processamento
desconto = valor * 0.05
valor_desc = valor - desconto

#saída
print("~ Resultado", "-"*21)
print(f"O valor da compra com o desconto de R${desconto:.2f} (5%),\n"
      f"será de R${valor_desc:.2f}.")

