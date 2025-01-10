"""
    Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se
 o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda

print("~ Formatando Moedas em Python", '-'*20)
preco = float(input("Informe um valor: R$"))
resp = str(input("Formatar? [S/N] ")).strip().upper()[0]
if resp == "S":
    dinheiro = True
    print("** Formatado...")
else :
    dinheiro = False
    print("** NÃO formatado...")
print("~ Resultado", '-'*38)
print(f"Aumentando o valor em 30%, {moeda.aumentar(preco, taxa=30, dinheiro=dinheiro)}")
print(f"Dimunindo o valor em 10%, {moeda.diminuir(preco, taxa=10, dinheiro=dinheiro)}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, dinheiro=dinheiro)}")
print(f"A metada de {moeda.moeda(preco)} é {moeda.metade(preco, dinheiro=dinheiro)}")
