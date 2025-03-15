def fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_sequence = fibonacci(n - 1)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


n = 6
print(fibonacci(n))
