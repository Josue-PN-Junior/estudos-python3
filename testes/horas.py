import datetime
while True :
    # Obtém a data e hora atual
    agora = str(datetime.datetime.now().time())[:5]
    time_ = agora
    n0 = " _ | ||_|"
    n1 = "  |"
    n2 = " _  _||_ "
    n3 = " _  _| _|"
    n4 = "   |_|  |"
    n5 = " _ |_  _|"
    n6 = " _ |_ |_|"
    n7 = " _   |  |"
    n8 = " _ |_||_|"
    n9 = " _ |_| _|"
    l = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

    hora = """    t0t1   t2t3
    m0m1 . m2m3
    b0b1 . b2b3\n"""

    cont = 0
    #print(time_)
    for n in time_ :
        if ":" == n :
            continue
        set = int(n)
        trocar = str(cont)
        if cont == 0 and n == "0" :
            hora = hora.replace("t0", "   ")
            hora = hora.replace("m0", "   ")
            hora = hora.replace("b0", "   ")
            cont += 1
            continue
        if n == "1" :
          hora = hora.replace("t"+ trocar, "   ")
          hora = hora.replace("m" + trocar, l[set][0:3])
          hora = hora.replace("b" + trocar, l[set][0:3])
          cont += 1
          continue
        hora = hora.replace("t"+ trocar, l[set][0:3])
        hora = hora.replace("m" + trocar, l[set][3:6])
        hora = hora.replace("b" + trocar, l[set][6:])
        cont += 1
    print(hora)
    print("\n" * 9)

#print(agora)
