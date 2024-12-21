num = list(range(1, 11))
print(num)
print(f"Tamnho da lista {len(num)}")
num.append(1)
print(num)
num.remove(1) # vai apagar o primeiro que ele encontrar
print(num)
if 11 in num:
    num.remove(11) # da erro se não tiver
else :
    print("Não achei")

# valores = [] da no mesmo
valores = list()
valores.append(1)
valores.append(2)
valores.append(1)
for v in valores:
    print(f'{v}', end=" ")

print("\n\nLista enumerada:")
for i, v in enumerate(valores):
    print(f"Na posição {i} encontrei {v}")

print("\n")
val = list()
for c in range(1, 3) :
    val.append(int(input("N: ")))
print(val)