# salário com 15% de aumento

#entrada
print("~ Reajuste Salarial", "-"*36)
sal = float(input("Qual é o salário atual do(a) funcionário(a): R$"))

# processamento
aumento = sal * 15 / 100
novo_sal = sal + aumento

# saída
print("~ Resultado", "-"*44)
print(f"O salário vai receber um aumento de 15%, R${aumento:.2f}.\n"
      f"O novo salário será de R${novo_sal:.2f}")