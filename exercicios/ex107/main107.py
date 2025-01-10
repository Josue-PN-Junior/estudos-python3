"""
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda

print("~ Exercitando módulos em Python", '-'*18)
din = float(input("Digite um valor: R$"))
print("~ Resultado", '-'*38)
print(f"O dobro de R${din} é R${moeda.dobro(din)}.")
print(f"A metade de R${din} é R${moeda.metade(din)}.")
print(f"Aumentando R${din} em 50% fica R${moeda.aumentar(din,50)}.")
print(f"Diminuindo R${din} em 50% fica R${moeda.diminuir(din, 50)}.")