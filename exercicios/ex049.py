"""
  Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

print("~ Tabuada v.2.0", '-'*34)
num = int(input("Informe um número: "))
print("\n~ Resultado", '-'*38)
print(f"= TABUADA DO {num} ====")
for i in range(0, 11) :
    print(f" {i:2} X {num} = {i*num}")