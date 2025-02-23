def multiplicar(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiplicar(a, b - 1)
    if b < 0:
        return -multiplicar(a, -b)


a = 5
b = 4 
print("Resultado de la multiplicación:", multiplicar(a, b))
