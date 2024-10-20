n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"Sua nota foi {media:.1f}")
if media >= 6 :
    print("A sua média foi boa ! PARABÉNS!")
else :
    print("Sua média foi ruim! ESTUDO MAIS!")
print("--FIM--")
