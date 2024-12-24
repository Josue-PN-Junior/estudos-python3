# dicionário
pessoas = {
    'nome': "Gustavo",
    'sexo': 'M',
    'idade': 21}
print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())
print(pessoas)

print('\nMostrando:')
# acessar dados
for k, v in pessoas.items():
    print(f"O {k} é igual o {v}!")

print("\nAlterando nome: ")
pessoas['nome'] = 'lucas'
print(pessoas['nome'])