a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)

print("\nListas:")
c = [0, 9 , 8, 7, 6]
d = c
print(c)
print(d)
print("Listas alteradas:") # as duas foram por serem lincadas
d[0] = 10
print(c)
print(d)

print("Criar cópia: ")
e = d[:] # cópia de d
print(e)
print(d)
print("Valores alterados na cópia")
e[2] = 19
print(e)
print(d)