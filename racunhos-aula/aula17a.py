num = [2, 5, 9 ,1]
print(num)
num[2] = 3
print(num)
# num[4] = 4 Não funciona
num.append(4) # tem que ser assim...
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(1, 9) # indice 1 adiciona o número 9
print(num)
num.pop(1)
print(num)
num.pop() # apaga o último item da lista
print(num)
del num[0] # apaga o item
print(num)
num.remove(3) # apaga o item 3
print(num)