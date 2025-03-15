numero = 5 
resultado: int


def factorial(n)->int:
    res:int = 1
    for i in ramge(1, n + 1):
        res = res * i
    return res


print(factorial(numero))