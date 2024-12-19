"""
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print("~ Lista de Preços com Tupla", '-'*22)
produtos = ("Leite", 5.5, "Pão", 0.5, "Papel", 15.99, "Queijo", 5.5, "Lápis", 1, "Borracha", 0.10)
print('- '*30)
print(f"{"Lista de Produtos":^60}")
print('- '*30)
for p in range(0, len(produtos), 2) :
    print(f"   {f"{produtos[p]} ":.<40}{f" R${produtos[p+1]:10.2f}"}")
print("- "*30)
print("> Fim da lita")
print(produtos)