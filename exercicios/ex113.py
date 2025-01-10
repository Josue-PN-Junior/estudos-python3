"""
    Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
 número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            n = int(n)
        except KeyboardInterrupt:
            print("\033[33mUsuário preferiu não informar um número...\033[m")
            break

        except:
            print("\033[31mERRO: Por favor, digite um número inteiro válido!\033[m")
            continue
        else:
            return n
            break
    return 0

def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            n = float(n)
        except KeyboardInterrupt:
            print("\033[33mO usuário não quis informar um número real...\033[m")
            break
        except:
            print("\033[31mERRO\033[m")
            continue
        else:
            return n
            break

    return 0.0


# __ Programa Principal __
print("~ Funções aprofundadas em Python", '-'*17)
num = leiaInt("Digite um número INTEIRO: ")
numFloat = leiaFloat("Digite um número REAL: ")
print("~ Resultado", '-'*38)
print(f"Valores digitados, inteiro {num} e real {numFloat}")