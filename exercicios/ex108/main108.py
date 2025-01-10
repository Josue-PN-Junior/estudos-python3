"""
    Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
 os números como um valor monetário formatado.
"""
import moeda

print("~ Formatando Moedas em Python", '-'*20)
p = float(input("Qual é o preço: R$"))
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"Aumentando 10%, de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Diminuindo 30%, de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 30))}")