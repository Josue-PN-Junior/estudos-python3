"""
    Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela
 algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
import moeda

print("~ Reduzindo ainda mais seu programa", '-'*14)
preco = float(input("Informe um preço: R$"))
print("~ Resultado", '-'*38)
moeda.resumo(preco, 50, 10, True)
moeda.resumo(preco, 30, 5, False)