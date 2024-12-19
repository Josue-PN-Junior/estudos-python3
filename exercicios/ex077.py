"""
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
print("~ Contando vogais em Tupla", '-'*13)
palavras = ("Casa", "Carro", "Vaca", "Luva", "Joelho", "Tatu", "Lasanha",
            "Biscoito", "Bolacha", "Balao", "Pipoca", "Shampoo", "Fusca",
            "Vigor", "Jogo", "Games", "Tabuleiro", "Memoria", "Mar",
            "Manga", "Dinossauro", "Paralepipedo", "Trabalho", "Chapeu",
            "Abacate", "Ameixa", "AAA")
for p in palavras:
    print("\n" + '-' * 50)
    print(f"Vógais em {p}: ", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
print("\n"+"-"*50, "\n> FIM")
