"""
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
 jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
 dado não tenha sido informado corretamente.
"""
def ficha(nomeJ="<desconhecido>", g=0):
    print(f"O jogador {nomeJ} fez {g} gol(s) no campeonato...")



# __ Program Principal __
print("~ Ficha do Jogador", '-'*31)
nome = str(input("Nome do jogador: ")).strip().capitalize()
gols = input(f"Quanto(s) gol(s) foram feitos? ")
print("~ Resultado", '-'*38)
# if nome == '':
#     if not gols.isnumeric():
#         ficha()
#     else :
#         gols = int(gols)
#         ficha(g=gols)
# else :
#     if gols.isnumeric():
#         gols = int(gols)
#         ficha(nome, gols)
#     else :
#         ficha(nome)
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome,g=gols)


print()
ficha()