"""
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print("~ Jogo do Par ou Ímpar", '-'*27)
vitorias = 0
while True:
    # número pc
    sorteado = randint(0,10)
    # escolha impopar
    while True:
        escolha = str(input("PAR OU IMPAR? [P/I] ")).strip().upper()[0]
        if escolha not in "PI":
            print("* Opção invalida *")
        else:
            break
    # escolha valor
    num = int(input("Digite um valor: "))
    # soma
    soma = num + sorteado
    # verificação ímpar ou par
    print("- "*26)
    print(f"!!! Você jogou {num} o computador {sorteado}")
    print("- "*26)
    if soma % 2 == 0 :
        print(f"@ RESULTADO: {soma} é PAR!")
        impar = False
    else :
        print(f"@ RESULTADO: {soma} é ÍMPAR!")
        impar = True
    # resultado
    if escolha == "I" and impar:
        print("* Vitória do jogador!")
        vitorias += 1
    elif escolha == "P" and not impar:
        print("* Vitória do jogador!")
        vitorias += 1
    else:
        print("DERROTA do jogador!")
        print("^"*50)
        break
    print('-'*50)
print(f"> Jogador derrotado com {vitorias} vitórias consecutivas!")