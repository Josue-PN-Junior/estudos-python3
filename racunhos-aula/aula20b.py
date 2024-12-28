def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# empacotameto
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"A soma dos {valores} = {s}")


# __ Programa Principal __
valores = [1, 2 , 3, 4, 5]
print("Valores:")
print(valores)
dobra(valores)
print("Valores dobrados: ")
print(valores)

print("\n\n")
soma(1, 2)
soma(1, 2, 3, 4, 5)
soma(1)