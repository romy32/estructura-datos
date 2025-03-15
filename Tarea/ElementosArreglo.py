def suma_arreglo(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + suma_arreglo(arr[1:])

arr = [1, 8, 3, 6, 5] 
print("Suma de los elementos:", suma_arreglo(arr))
