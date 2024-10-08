# Conversor de Medidas de metros para outras...

#entrada
print("~ Conversor de Medidas", "-"*20)
metros = float(input("Informe uma medida em metros: "))

#processamento
dm = metros * 10
cm = dm * 10
mm = cm * 10
dam = metros / 10
hm = dam / 10
km = hm / 10

# saída
print("~ Resultado", "-"*25)
print(f"A medida de {metros}m corresponde: \n"
      f"Quilômetros: {km}km\n"
      f"Hectômetro: {hm}hm\n"
      f"Decâmetro: {dam}dam\n"
      f"Decímetro: {dm}dm\n"
      f"Centímetro: {cm}cm\n"
      f"Milímetro: {mm}mm")