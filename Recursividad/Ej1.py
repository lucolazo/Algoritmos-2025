# 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un 
# número dado.

def fibonacci (n: int):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(5))