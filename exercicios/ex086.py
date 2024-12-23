"""
    Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.
"""
print("~ Matriz em Python", '-'*31)
matriz = [
    [],
    [],
    []
]
# outra forma seria colocar todos os valores em listas...
for index in range(0, 3):
    for indexC in range(0, 3):
        matriz[index].append(int(input(f"Informe o valor da linha {index} e coluna {indexC}: ")))
print("~ Resultado", '-'*38)
print("Matriz: ")
for linha in matriz:
    print("\t| ", end='')
    for valorC in linha:
        print(f"{valorC:^5}", end=" | ")
    print(end="\n")