from time import sleep
from libs.texto import *
from libs.validacao import *
from libs.arquivo import *

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

print("~ Programa final", '-'*33)
while True:

    r = []
    sleep(0.5)
    r = menu(["Ver Pessoas Castradas", "Cadastrar Nova Pessoa", "\033[31mSair do Sistema\033[m"], "Menu Principal", retorno=True)
    escolha = leiaInt("Escolha a opção: ")
    if escolha == 0 or escolha == len(r):
        print(f"\033[31mSaindo do sistema... ", end='')
        sleep(1)
        break
    if 0 < escolha <= len(r):
        setTitulo(menu(r, retornoOp=escolha))
        if escolha == 1:
            lerArquivo(arq)
            sleep(3)

        elif escolha == 2:
            nome = str(input("Informe o nome: ")).strip().title()
            idade = leiaInt("Informe a idade: ")
            escreverArquivo(arq, nome, idade)

    else :
        print("\n\033[31m!!! Opção iformada não existe!\033[m\n")
print(f"finalizado!\033[m")