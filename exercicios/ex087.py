"""
    Aprimore o desafio anterior, mostrando no final:
 A) A soma de todos os valores pares digitados.
 B) A soma dos valores da terceira coluna.
 C) O maior valor da segunda linha.
"""
print("~ Mais sobre Matriz em Python", '-'*20)
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Iforme o valor posição [{l}, {c}]: ")))
print("~ Resultado", '-'*38)
soma = somaL3 = somaC3 = 0
print("Matriz:")
for i, l in enumerate(matriz):
    print('\t', end='')
    for p, c in enumerate(l):
        print(f"[{c:^5}] ", end='')
        if c % 2 == 0:
            soma += c
        if i == 2:
            somaL3 += c
        if p == 2:
            somaC3 += c
    print()
print("- "*26)
print(f"+ Soma dos valores pares da matiz: {soma}")
print(f"# Soma dos valores da 3ª linha: {somaL3}")
print(f"* Soma dos valores da 3ª coluna: {somaC3}")
print(f"^ O maior valor da 2ª coluna: {max(matriz[1])}")