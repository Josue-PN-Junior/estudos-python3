def setTitulo(msg):
    print('~ '*26)
    print(f"{msg:^50}")
    print('~ '*26)

def menu(opc, titulo="MENU", retorno=False, retornoOp=0):
    print("\n\n\n\n")
    if retornoOp != 0:
        selecionado = opcoes(opc, showOp=retornoOp)
        return selecionado
    setTitulo(titulo)
    opcoes(opc)
    if retorno:
        return opc


def opcoes(opc, showOp=0):
    if showOp == 0:
        for n, opcoes in enumerate(opc):
            print(f"\t{n+1:^2} - {opcoes}")
        print("_-"*26)
    else :
        return opc[showOp-1]

