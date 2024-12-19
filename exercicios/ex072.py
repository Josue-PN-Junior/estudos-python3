"""
    Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
print("~ Número por Extenso", '-'*29)
tuplaNum = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenovo", "vinte")

while True:
    verNum = int(input("Selecione um número de 0 a 20: "))
    while verNum < 0 or verNum > 20:
        verNum = int(input("O número deve ser entre 0 e 20: "))
    print("~ Resultado", '-' * 38)
    print(f"O número selecionado foi \033[33m{tuplaNum[verNum]}\033[m")

    while True:
        resp = str(input("\n> Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "NS" :
            break

    if resp == "N" :
        break

print("Programa encerrado!")