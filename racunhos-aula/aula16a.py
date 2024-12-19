lanche = ("Hamburgue", "Suco", "Pizza", "Pudim")
# lanche1 = "sorvete", "hamburgue", "suco", "pudim"
print(lanche)
# print(lanche1)
print(lanche[2:4])
# Você pode sobreescrever
lanche = "Frango", "Chocolate", "Sorvete", "Pão"
print(lanche, '\n\n')
# mas não pode ser mudada
# lanche[1] = "Queijo"     /////////// Não pode
for comida in lanche :
    print(f"Eu posso comer {comida}")
print("Vou comer...\n\n")

# dá pra passar pra outra
lanche2 = lanche
print(lanche2)

# mostrar a posição
for cont in range(0, len(lanche)):
    print(f"{cont+1}ª(indice {cont}) comida {lanche[cont]}")
print("\n\n")

# pega a posição e o item
for pos, comida in enumerate(lanche):
    print(f"Comida indice {pos} = {comida}")
print("\n\n")

print(lanche)
# ordena
print(sorted(lanche))
# mas não muda
print(lanche)
print(type(lanche))
print("\n\n")

# vira uma lista
lanche3: tuple = sorted(lanche)
print(lanche3)
print(type(lanche3))
print("\n\n")

# aumento de itens em sobreescrever
lanche4 = lanche
print(lanche4)
lanche4 = ("Suco1", "Suco2", "Suco3", "Suco4", "Suco5")
print(lanche4)
# funciona