estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("UF: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())

print(brasil)