"""
  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
 Exemplos de palíndromos:
 APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

print("~ Detector de Palíndromo", '-'*25)
frase = str(input("Digite uma frase: ")).strip().upper()
# tirar os espaços
frs = frase.split()
frs = ''.join(frs)
frs1 =  ""
# frs1 = frase[::-1] inverte
for i in frs :
    frs1 = i + frs1

print("\n~ Resultado", '-'*38)
if frs == frs1 :
    print(f"A frase {frase} é um PALÍNDROMO!")
else :
    print("A frase não é um palíndromo...")