"""
    Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

 – EQUILÁTERO: todos os lados iguais

 – ISÓSCELES: dois lados iguais, um diferente

 – ESCALENO: todos os lados diferentes
"""
print("~ Analisando Triângulos v2.0", '-'*21)
rt1 = float(input("Informe o primeiro segmento de reta: "))
rt2 = float(input("Informe o segundo segmento de reta: "))
rt3 = float(input("Informe o terceiro segmento de reta: "))
# processamento e saída
print("~ Resultado", '-'*38)
if rt1 + rt3 > rt2 and rt1 + rt2 > rt3 and rt2 + rt3 > rt1 :
    if rt1 == rt2 == rt3 :
        print("* \033[032mÉ possível\033[m formar um triângulo \033[034mEQUILÁTERO\033[m!")
    elif rt1 == rt2 or rt1 == rt2 or rt2 == rt3 :
        print("* \033[032mÉ possível\033[m formar um triângulo \033[034mISÓSCELES\033[m!")
    else :
        print("* \033[032mÉ possível\033[m formar um triângulo \033[034mESCALENO\033[m!")
else :
    print(f"! \033[031mNÃO é possível formar um triângulo\033[m !")