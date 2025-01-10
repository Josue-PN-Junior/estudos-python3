try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print("ERRO")
    print(erro)
    print()
    print(erro.__cause__)
    print()
    print(erro.__class__)
else:
    print(f"Resultado {r}")

try:
    a = int(input("N: "))
    b = int(input("D: "))
    r = a / b
except ZeroDivisionError:
    print(F"Zero não pode!")
else :
    print(f"Boa!")