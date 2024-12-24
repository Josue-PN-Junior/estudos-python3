brasil = []
estado1 = {'uf': "Rio de Janeiro", 'sigla': "RJ"}
estado2 = {'uf': "São Paulo", 'sigla': "SP"}
brasil.append(estado1)
brasil.append(estado2)

print("Lista: ", end='')
print(brasil)
print("Item: ", end='')
print(brasil[1])
print("Sigla: ", end='')
print(brasil[1]['sigla'])