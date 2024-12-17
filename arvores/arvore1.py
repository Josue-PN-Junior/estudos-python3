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

    def ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no.esq:
            self.ordem(no.esq)
        print(no, end=' ')
        if no.dir:
            self.ordem(no.dir)

class ArvoreBinBusca(ArvoreBin):
    def busca(self, sinal):
        return self._busca(sinal, self.raiz)

    def _busca(self,  sinal, no=None):
        if no is None:
            no = self.raiz
        if no.esq and (sinal == "." or sinal == "?"):
            self._busca(sinal, no.esq)
        print(f"Olha : {item}, {no}")
        if no.dir and (sinal == "." or sinal == "?"):
            self._busca(sinal, no.dir)

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
    itens = ['-', '.', '?']
    for item in itens :
        if item[0] == '-' :
            arvore._busca(item, n8)
        elif item[0] == '.' :
            arvore._busca(item, n1)
        else :
            arvore._busca(item, n1)
            arvore._busca(item, n8)



