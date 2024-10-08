# converte reais em dólares

# entrada
print("~ Conversor de Moedas", "-"*10)
reais = float(input("Quantos reais você possuí: R$"))

#processamento, calculo de conversão
dol = reais / 5.46 #valor do Dólar ´-´
euro = reais / 5.99 #valor do Euro
yen = reais / 0.03668 #valor Iene

# saída
print("~ Resultado", "-"*5)
print(f"Com R${reais} você pode comprar US${dol:.2f} (doláres)!")
print(f"ou \u00A5{yen:.2f} (Ienes) ou \u20AC{euro:.2f} (Euros)!")