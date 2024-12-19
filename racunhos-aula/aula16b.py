# ele não soma
a = (1, 2 , 3, 4)
b = (4, 5, 6 , 7 ,8)
c = a + b
d = b + a
# são diferentes
print(c)
print(d)
# mostra a posição de 3
print(c.index(3))
print("\nCount")
# mostra a posição quantas vezes aparece
print(c.count(4))
print(c.count(1))

print("\n\n")
# pessoa
pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)

# apaga a tupla
del(pessoa)
print(pessoa)