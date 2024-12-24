"""
    Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
 do aproveitamento de cada jogador.
"""
print("~ Aprimorando os Dicionários", '-'*21)
jogadores = list()
jogador = dict()
gols = []
cont = 0
while True:
    cont += 1
    print(f"{f"----- {cont}º Jogador ":-<50}")
    jogador['nome'] = str(input("Nome: "))
    part = int(input(f"Quantas partidadas {jogador['nome']} jogou? "))
    jogador['partidas'] = part
    for golsP in range(1, part+1):
        gols.append(int(input(f"\t- Quantos gols ele(a) fez na {golsP}ª partida? ")))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        resp = str(input("\n> Quer continuar a adicionar jogadores? [S/N] ")).strip().upper()[0]
        if resp in "NS":
            break
    if resp == "N":
        break

print("\n~ Resultado", '-'*38)
for c, jog in enumerate(jogadores):
    print(f"\tCOD: {c} * {jog['nome']} jogou {jog['partidas']} partidas, total de gols: {jog['total']}.")
print("- "*26)
while True:
    numJog = int(input("> Quer ver os resultados de qual jogador(a)? [999 iterrompe] "))
    if numJog == 999:
        print(f"Encerrando...")
        break
    if numJog < len(jogadores) and numJog >= 0:
        for v, dic in enumerate(jogadores):
            if v == numJog:
                print(f"\tJOGADOR(A): {dic['nome']}")
                print(f"\tPARTIDAS: {dic['partidas']}")
                print(f"\tTOTAL GOLS: {dic['total']}")
                for p, g in enumerate(dic['gols']):
                    print(f"\t- Na {p+1} partida fez {g}")
                break
    else :
        print("\n**Jogador não encontrado...")

print(f"{f" ENCERRADO ":-^50}")