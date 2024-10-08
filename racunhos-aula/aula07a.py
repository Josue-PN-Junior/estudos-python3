nome = input("Qual é o seu nome? ")
print(f"Prazer em te conhecer {nome:~^10} !")
print("-"*40)
n1 = int(input("Digite um valor: "))
n2 = int(input("digite outro valor: "))
print("~ Resultado", "="*20)
print(f"A soma de {n1} + {n2} vale {n1+n2}!")
print(f"A divisão é {n1/n2}\n"
      f"O resto é {n1%n2}\n"
      f"A divisão inteira é {n1//n2}\n"
      f"A multiplicação é {n1*n2}\n"
      f"A potência é {n1**n2}")