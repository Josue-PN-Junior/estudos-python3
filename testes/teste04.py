from typing import List

grid = [
    "   ",
    " h ",
    "   ",
]
def find_snake_on_grid(grid: List[str]) -> List[List[int]]:
    # Verificar se a cobra
    for busca in grid:
        if 'h' in busca:
            temCobra = True

    if not temCobra:
        return []

    linha = len(grid)

    for linha in range(linha):
        corpo = False
        linhaY = grid[linha]
        if linhaY.find('h') != -1:
            lista = ([[linhaY.find('h'), linha]])
            # se cabeça já encontrada
        if ('<' or '>' or 'v' or '^') in linhaY:
            corpo = True

    # cabeça já encontrada
    passar = len(grid) * len(grid[0])
    for caracater in range(passar):
        ultimo = lista[len(lista) - 1]
        cordX = ultimo[0]
        cordY = ultimo[1]

        if (cordY - 1) <= (len(grid) - 1):
            if (grid[cordY - 1][cordX] == 'v'):
                lista.append([cordX, cordY - 1])

        if (cordY + 1) <= (len(grid) - 1):
            if (grid[cordY + 1][cordX] == '^'):
                lista.append([cordX, cordY + 1])

        if (cordX + 1) <= (len(grid[0]) - 1):
            if (grid[cordY][cordX + 1] == '<'):
                lista.append([cordX + 1, cordY])

        if (cordX - 1) <= (len(grid[0]) - 1):
            if (grid[cordY][cordX - 1] == '>'):
                lista.append([cordX - 1, cordY])

    print(lista)

    return lista