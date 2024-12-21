"""
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
 se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
print("~ Validando expressões matemáticas", '-'*15)
expressao = str(input("Digite uma expessão mátematica: "))
listaDig = list()
for dig in expressao:
    listaDig.append(dig)
print("~ Resultado", '-'*38)
cont = 0
for v in listaDig:
    # dá saldo para poder fechar!
    if v == '(' :
        cont += 1
    # tira saldo quando fecha
    if v == ')' :
        cont -= 1
        # se fechou sem abrir já está automaticamente errada
        if cont == -1:
            break
# se saldo não for zero significa que algum ( ficou aberto ou que algum foi fechado sem necessidade
if cont == 0:
    print("\033[32mExpressão válida!\033[m")
else :
    print("\033[31m* Expressão inválida!\033[m")
pilha = []
for p in expressao:
    if p == ('('):
        pilha.append("(")
    if p == (')'):
        if len(pilha) > 0 :
            pilha.pop()
        else :
            pilha.append(")")
            break
if len(pilha) > 0:
    print("Expressão INVÁLIDA!")
else :
    print("Expressão VÁLIDA!")