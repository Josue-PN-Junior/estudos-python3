class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.dado)


class ArvoreBin:
    def __int__(self, dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None


class ArvoreBinBusca(ArvoreBin):

    def buscaEsq(self, no=None):
        if no:
            return no.esq

    def buscaDir(self, no=None):
        if no:
            return no.dir

    def _busca(self, sinal, n, no=None):
        lista = []
        if no is None:
            no = self.raiz
        if n == 0 :
            if item[0] == '-' :
                print("Traço", no.dir)
                lista.append(str(no.dir))
                return lista
            elif item[0] == '.':
                print("Ponto", no.esq)
                lista.append(str(no.esq))
                return lista
            else :
                lista.append(str(no.esq))
                lista.append(str(no.dir))
                return lista



        if n == 1:
            tem = self._busca(item, 0, no)
            if tem[0] == "E" :
                print("Retornou E")
                if item[1] == '.':
                    print("Traço", no.dir)
                    val = self.buscaDir(no.dir)
                    lista.append(str(val))
                    return lista
            elif tem[0] == "T":
                if item[1] == '-':
                    print("Ponto", no.esq)
                    val = self.buscaEsq(no.esq)
                    lista.append(str(val))
                    return lista
                else:
                    val = self.buscaEsq(no.esq)
                    lista.append(str(val))
                    val = self.buscaDir(no.dir)
                    lista.append(str(val))


                    print("?????", no.dir, no.esq)
                    return lista










if __name__ == "__main__":
    arvore = ArvoreBinBusca()
    n = No('start')
    n1 = No("E")
    n2 = No("I")
    n3 = No("S")
    n4 = No("U")
    n5 = No("A")
    n6 = No("R")
    n7 = No("W")
    n8 = No("T")
    n9 = No("N")
    n10 = No("D")
    n11 = No("K")
    n12 = No("M")
    n13 = No("G")
    n14 = No("O")

    n.dir = n8
    n.esq = n1
    n1.dir = n5
    n1.esq = n2
    n2.dir = n4
    n2.esq = n3
    n5.dir = n7
    n5.esq = n6
    n8.dir = n12
    n8.esq = n9
    n9.dir = n11
    n9.esq = n10
    n12.dir = n14
    n12.esq = n13
    arvore.raiz = n
    itens = ["--"]
    for item in itens :
        tm = len(item)-1
        print(arvore._busca(item, tm, n))




