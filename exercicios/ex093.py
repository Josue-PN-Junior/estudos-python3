"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
 quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
 guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
total = 0
aproveitamento = {}
gols = {}
print("~ Cadastro de Jogador de Futebol", '-'*17)
nomejogador = str(input("Nome do jogador: ")).strip().capitalize()
partidas = int(input("Quantas partidaas ele jogou? "))

print("- "*26)
aproveitamento['nome'] = nomejogador
aproveitamento['partidas'] = partidas
for p in range(1, partidas+1):
    qt_gols = int(input(f"- Quantos GOLS ele fez na {p}ª partida: "))
    gols[f'partida{p}'] = qt_gols
    total += qt_gols
gols['total'] = total
aproveitamento['gols'] = gols.copy()

print("~ Resultado", '-'*38)
print(f" @ JOGADOR: {aproveitamento['nome']}")
print(f" - PARTIDAS: {aproveitamento['partidas']}")
print(f" - TOTAL DE GOLS: ", end="")
for v, k in aproveitamento.items():
    if v == 'gols':
        print(f"{k['total']}")
print()
while True:
    m = int(input("> Mostrar aproveitamento de qual partida? [0 interrompe]  "))
    if m == 0:
        print("Finalizando...", end=" ")
        break

    if m <= aproveitamento['partidas'] and m > 0 :
        print(f" # Na {m}ª PARTIDA {aproveitamento['nome']} fez {aproveitamento['gols'][f'partida{m}']} gols")
    else:
        print("** Partida não encontrada.")
    print("- "*26)
print("PROGRAMA ENCERRADO!")


