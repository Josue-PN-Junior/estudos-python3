def arquivoExiste(arq):
    try:
        a = open(arq, "rt")
        a.close()
        return True
    except :
        return False


def criarArquivo(arq):
    try:
        a = open(arq, "wt+")
        a.close()
        print(f"** Arquivo {arq} criado com sucesso!")
    except:
        print("** Ocorreu um ERRO na criação do arquivo!")


def lerArquivo(arq):
    try:
        a = open(arq, "rt")
    except :
        print("** ERRO")
    else :
        pessoas = str(a.read()).strip().split('\n')
        for i, p in enumerate(pessoas):
            cad = p.split(';')
            print(f"   {f"{cad[0]} ":.<37} {cad[1]} anos")
    finally:
        a.close()


def escreverArquivo(arq, nome="ERRO", idade=0):
    try:
        a = open(arq, "at+")
        a.write(f"{nome};{idade}\n")
        a.close()
        print(f" \033[33m* Pessoa cadastrada!\033[m")
    except:
        print(f"\033[31mNão foi possível cadastrar uma pessoa no arquivo \033[m{arq}\033[31m!\033[m")