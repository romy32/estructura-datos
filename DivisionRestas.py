def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    if a < b:
        return 0
    return 1 + dividir(a - b, b)


a = 40
b = 2 
print("Resultado de la división:", dividir(a, b))