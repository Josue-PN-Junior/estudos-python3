"""
  Crie um programa que leia dois valores e mostre um menu na tela:

 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa

 Seu programa deverá realizar a operação solicitada em cada caso.
"""

menu = {
    1 : "+  S O M A D O R  +",
    2 : "* M U L T I P L I C A D O R *",
    3 : "^ M A I O R - N Ú M E R O ^",
    4 : "! INFORMANDO NOVOS NÚMEROS !",
    5 : "... Saindo ..."
}

print("~ Criando um Menu de Opções", '-'*22)
num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
fim = False
while not fim :
    # Menu
    print("\n"+"="*50)
    print(f"{" M E N U ":^50}")
    print("-"*50)
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
\033[31m[ 5 ] Sair do programa\033[m""")
    # Fim Menu
    print("-"*50)
    # Opção
    opc = int(input("Informe a opção: "))

    # Teste Menu
    if opc < 1 or opc > 5 :
        print(f"\033[31m{"! Opção invalida !":^50}\033[m")

    # Se Verdadeiro
    else :
        print(f"\n\033[33m{menu[opc]:^50}\033[m")
        print('\n' + "- " * 26)

        # Opções

        if opc == 1 :
            print(f"A soma de {num1} + {num2} é igual: {num1 + num2}!")

        elif opc == 2 :
            print(f"A produto da multiplicação de {num1} por {num2} é: {num1*num2}")

        elif opc == 3 :
            if num1 == num2 :
                print(f"Os números {num1} e {num2} são iguais!")
            elif num1 > num2 :
                print(f"O número {num1} é MAIOR que o número {num2}!")
            else :
                print(f"O número {num2} é MAIOR que o número {num1}!")

        elif opc == 4 :
            num1 = int(input("Informe um novo número para o primeiro valor: "))
            num2 = int(input("Informe um novo valor para o segundo número: "))
            print(f"\nNovos valores informados: {num1} e {num2}!")

        elif opc == 5:
            fim = True
            print("> Encerrando...")

        print('- '*26)
print("Programa finalizado.")