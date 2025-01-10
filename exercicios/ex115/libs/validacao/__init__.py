def leiaInt(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            n = int(n)
        except KeyboardInterrupt:
            return 0
            break
        except:
            print("\033[31m!!! Por favor, informe um número válido!\033[m")
            continue
        else:
            if n == 0:
                print("\033[31m!!! ' 0 ' Não é válido!\033[m")
                continue
            return n
            break
    return 0

