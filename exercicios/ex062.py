"""
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print("~ Super Progressão Aritmética v3.0", '-'*15)
primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
print("~ Resultado", '-'*38)
mais = 10
termo = 1
# while termo <= 10 :
#     pa = primeiro + (termo - 1) * razao
#     termo += 1
#     print(f"{pa}", end=' ')
#
# mais = int(input("\n> Quer mostrar mais quantos termos? "))
while mais != 0 :
    fim = (termo+mais-1)
    termo = 1
    print(F"- Mostrando {fim} termos da PA!")
    while termo <= fim :
        pa = primeiro + (termo - 1) * razao
        termo += 1
        print(f"{pa}", end=' ')
    mais = int(input("\n\n> Quer mostrar mais quantos termos? "))
    print('-'*50)
print(f"{"Fim":^50}")