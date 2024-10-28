"""
  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
from itsdangerous.encoding import int_to_bytes

cor = {
    "Verme" : "\033[31m",
    "Cin" : "\033[37m",
    "Amar" : "\033[33m",
    "Ver" : "\033[32m",
    "Mag" : "\033[35m"
}


print("~ Conversor de Bases Numéricas", '-'*19) #31
num = int(input("Informe um número inteiro a ser convertido: "))
#opções
print("|_____________________|" + '_'*27)
print(f"| {cor["Amar"]}Opções de conversão\033[m |")
print("|---------------------|")
print(f"|  {cor["Cin"]}( 1 ) Binário\033[m      |")
print(f"|  {cor["Ver"]}( 2 ) Octal\033[m        |")
print(f"|  {cor["Mag"]}( 3 ) Hexadecimal\033[m  |")
print("|_____________________|")
escolha = int(input(f"{cor["Amar"]}*\033[m Escolha uma opção: "))

# condições
print("\n~ Resultado", '-'*38)

# processamento
if escolha == 1 :
    print(f"@ {escolha} {cor["Cin"]}Convertido para BINÁRIO é :\033[m {bin(num)[2:]}")

elif escolha == 2 :
    print(f"@ {escolha} {cor["Ver"]}Convertido para OCTAL é :\033[m {oct(num)[2:]}")
elif escolha == 3 :
    print(f"@ {escolha} {cor["Mag"]}Convertido para HEXADECIMAL é :\033[m {hex(num)[2:]}")
else :
    print(f"{cor["Verme"]}OpçãoINVALIDA!\033[m")