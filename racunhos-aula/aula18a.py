teste = list()
teste.append("Gustavo")
teste.append(40)
pessoas = []
pessoas.append(teste[:])
print(pessoas)
galera = [["Karlos", 10], ["Maicon", 20], ["Fábio", 10]]
print(galera[:][:])
print("\n\n")

for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade!")

print()
grupo = []
dado = []
for i in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    grupo.append(dado[:])
    dado.clear()

print(grupo)