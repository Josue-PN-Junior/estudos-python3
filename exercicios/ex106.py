"""
    Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
 aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""


def manual(c):
    t = 50
    print(f"\033[1;35;40;40m", end='')
    print("~"*t)
    print(f"{f"Acessando o comando \'{c}\'":^50}")
    print("~"*t)
    print(f"\033[m\033[34;40m")
    print(help(c))
    print("\033[m")

# __ Programa Principal __
print("~ Interactive helping system in Python", '-'*11)
while True:
    print("\033[1;32;40m", end='')
    print("~"*50)
    print(f"{"Interactive Help Python":^50}")
    print("~"*50)
    print("\033[m", end='')
    print("\033[1;35;40mDIGITE O COMANDO QUE GOSTARIA DE SABER ['FIM' para interromper] \033[m")
    comando = str(input("\033[35mComando: ")).strip().lower()
    print("\033[m", end="")
    if comando == "fim":
        print("\n\033[1;31;40mEncerrando...")
        break
    manual(comando)

print("PROGRAMA Finalizado.\033[m")