


def leiaDinheiro(msg):
    val = True
    while val:
        n = str(input(msg)).strip()

        if ',' in n:
            n = n.replace(',', '.')

        if n.isalpha() or n == "":
            print(f"\033[31mERRO: \'{n}\' não é um valor válido..\033[m")
        else:
            print(f"\033[32mValor válido\033[m")
            val = False
            return float(n)


