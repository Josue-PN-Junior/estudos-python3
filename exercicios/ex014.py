# Conversor de °C para °F

# entrada
print("~ Conversor de Temperaturas", "-"*30)
cel = float(input("Informe uma temperatura em Graus Celsius: °C "))

# processamentos
fi = cel * 1.8 + 32
# cel = ( 5 / 9 ) * ( fi - 32 )

# saída
print("~ Resultado", "-"*46)
print(f"** {cel}°C equivale a {fi:.1f}°F")

# fahrenheit
print("~ Conversor de Temperaturas", "-"*30)
fi = float(input("Informe uma temperatura em Graus Fahrenheit: °F "))
cel = ( 5 / 9 ) * ( fi - 32)
print("~ Resultado", "-"*46)
print(f"** {fi}°F equivale a {cel:.1f}°C")

