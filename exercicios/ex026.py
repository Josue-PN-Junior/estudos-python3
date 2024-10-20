"""
  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

# entrada
print("~ Primeira e última ocorrência de uma string", "-"*15) # 45 R12
texto = str(input("Escreva uma frase: ")).strip()

# processamento
qt_as = texto.upper().count('A')

# saída
print("~ Resultado", "-"*48)
print(f"A letra \"A\" aparece {qt_as} vezes na frase.")
print(f"A letra aparece pela primeira vez na posição {texto.upper().find("A")+1}.") # começando do 1 não 0
print(f"E ela aparece pela última vez na posição {texto.upper().rfind("A")+1}.")