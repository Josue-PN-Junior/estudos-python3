"""
    Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
 leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
 valores que seja monetários.
"""
from utilidadesCeV import moeda

print("~ Entrada de dados monetários", '-'*20)
preco = float(input("Informe um valor: R$"))
print("~ Resultado", '-'*38)
moeda.resumo(preco, 30, 10, True)
moeda.resumo(preco, 15, 90)
