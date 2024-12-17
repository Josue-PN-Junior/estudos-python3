from typing import List

def indiceUm(tm, sinal):
    if tm == 0:
        if sinal[0] == ".":
            lista = ["E"]
        elif sinal[0] == '-':
            lista = ["T"]
        else:
            lista = ["E", "T"]
    print(f"lista {lista}")
    return lista

def indiceDois(tm, sinal):
    if tm == 1 :
        if len(indiceUm(0, sinal)) == 2 :
            #print("primeiro = ?")
            if sinal[1] == "." :
                lista = []
                lista.append("I")
                lista.append("N")
                return lista
            elif sinal[1] == "-" :
                #print("Esse : ?-")
                lista = [
                    "A",
                    "M"
                ]
                return lista
            else :
                lista = []
                lista.append("I")
                lista.append("A")
                lista.append("N")
                lista.append("M")
                return lista
        else :
            if indiceUm(0, sinal)[0] == "T" :
                #print("Primiero é traço")
                if sinal[1] == ".":
                    lista = []
                    lista.append("N")
                elif sinal[1] == "-":
                    lista = []
                    lista.append("M")
                else:
                    lista = []
                    lista.append("N")
                    lista.append("M")
                return lista
            else :
                #print("Primiero é ponto")
                if sinal[1] == ".":
                    lista = []
                    lista.append("I")
                    return lista
                elif sinal[1] == "-":
                    lista = []
                    lista.append("A")
                    return lista
                else:
                    lista = []
                    lista.append("I")
                    lista.append("A")
                    return lista

word = "."
lista = []
for sinal in word:
    tm = len(sinal)-1
    # print(tm)
    # caso um caractere
    if tm == 0 :
        lista = []
        r = indiceUm(tm, sinal)
        return r

    # caso dois caractere
    if tm == 1:
        lista = []
        r = indiceDois(tm, sinal)
        print(r)
        return r


    if tm == 2 :
        if '?' in sinal :
            if sinal == "?-?":
                lista = [
                    "R",
                    "N",
                    "G",
                    "D"
                ]
                print(lista)
            elif sinal == "?.?":
                lista = [
                    "S",
                    "U",
                    "D",
                    "T"
                ]
                print(lista)
            elif sinal == "?..":
                lista = [
                    "S",
                    "D"
                ]
                print(lista)
            elif sinal == "?.-":
                lista = [
                    "U",
                    "K"
                ]
                print(lista)
            elif sinal == "?--":
                lista = [
                    "W",
                    "O"
                ]
                print(lista)
            elif sinal == "?-.":
                lista = [
                    "R",
                    "G"
                ]
                print(lista)
            print("Tem ?")
            print("Não tem ?")
            if len(indiceDois(1, sinal)) == 4 :
                #print("segundo = ?")
                if sinal[2] == "." :
                    lista = []
                    lista.append("S")
                    lista.append("R")
                    lista.append("D")
                    lista.append("G")
                    print(lista)
                elif sinal[2] == "-" :
                    lista = []
                    lista.append("U")
                    lista.append("W")
                    lista.append("K")
                    lista.append("O")
                    print(lista)
                else :
                    lista = []
                    lista.append("S")
                    lista.append("U")
                    lista.append("R")
                    lista.append("W")
                    lista.append("D")
                    lista.append("K")
                    lista.append("G")
                    lista.append("O")
                    print(lista)

            elif len(indiceDois(1, sinal)) == 2 :
                if indiceDois(1, sinal) == ['I', 'A'] :
                    #print("esses .?")
                    if sinal[2] == "." :
                        lista = [
                            "S",
                            "R"
                        ]
                        print(lista)
                    elif sinal[2] == "-" :
                        lista = [
                            "U",
                            "W"
                        ]
                        print(lista)
                    else :
                        lista = [
                            "S",
                            "U",
                            "R",
                            "W"
                        ]
                        print(lista)

            elif indiceDois(1, sinal) == ['N', 'M']:
                #print("eses -?")
                if sinal[2] == "." :
                    lista = [
                        "D",
                        "G"
                    ]
                    print(lista)
                elif sinal[2] == "-" :
                    lista = [
                        "K",
                        "O"
                    ]
                    print(lista)
                else :
                    lista = [
                        "D",
                        "K",
                        "G",
                        "O"
                    ]
                    print(lista)
        else :
            print("Não tem ? ")
            if sinal == "..." :
                print("S")
            elif sinal == "..-" :
                print("U")
            elif sinal == ".-." :
                print("R")
            elif sinal == ".--" :
                print("W")
            elif sinal == "-.." :
                print("D")
            elif sinal == "-.-" :
                print("K")
            elif sinal == "--." :
                print("G")
            elif sinal == "---" :
                print("O")
            else :
                print("")