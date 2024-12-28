"""
    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
 uma mensagem com tamanho adaptável.
 Ex: escreva(‘Olá, Mundo!’)
 Saída:          ~~~~~~~~~
                 Olá, Mundo!
                 ~~~~~~~~~
"""
def escreva(texto):
    t = len(texto)+4
    print('~'*t)
    print(f"{texto:^{t}}")
    print('~'*t)



# __ Programa Principal __
print("~ Um print especial", '-'*30)
msg = str(input("Escreva uma mensagem: "))
print()
print("~ Resultado", '-'*38)
print()
escreva(msg)