def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

def par(n=0):
    if n % 2 ==0 :
        return True
    else :
        return False

n = int(input("Valor: "))
res = fatorial(n)
print(res)
print(f"é par? {par(n)}")
