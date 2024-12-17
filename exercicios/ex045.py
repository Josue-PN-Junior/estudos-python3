"""
  Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random

cor = {
    "az" : "\033[34m",
    "am" : "\033[33m",
    "vd" : "\033[32m",
    "vr" : "\033[31m",
    "fc" : "\033[m"
}
jokenpo = {
    1 : "Pedra",
    2 : "Papel",
    3 : "Tesoura"
}

print(f"~ GAME: Pedra Papel e Tesoura", '-'*20)
maquina = random.randint(1,3)
# print(f"Escolha da máquina {maquina}")
print(f"{cor["am"]}*** Máquina já selecionol qual vai jogar ***{cor["fc"]} ")
while True:
    print(f"""
= =  JO - KEN - PO  = =
    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura
========================""")
    esc = int(input("Escolha: "))
    if esc >= 1 and esc <=3 :
        break
    else :
        print(f"\n{cor["vr"]}! Opção inválida ! {cor["fc"]}")
# resultado
print(f"\n  {cor["az"]}==={cor["fc"]} Máquina{cor["vr"]}  x  {cor["fc"]}Você{cor["az"]} ==={cor["fc"]}")
print(f"\n\t   {jokenpo[maquina]} x {jokenpo[esc]}")
print(f"\n{'-'*30}")
if esc == maquina :
    print(f"\t\t  {cor["am"]}EMPATE!{cor["fc"]}")
elif maquina == 1 and esc == 2:
    print(f"\t\t  {cor["vd"]}VITÓRIA{cor["fc"]}")
elif maquina == 2 and esc == 3:
    print(f"\t\t  {cor["vd"]}VITÓRIA{cor["fc"]}")
elif maquina == 3 and esc == 1:
    print(f"\t\t  {cor["vd"]}VITÓRIA{cor["fc"]}")
else :
    print(f"\t\t  {cor["vr"]}DERROTA!{cor["fc"]}")
print('-' * 30)