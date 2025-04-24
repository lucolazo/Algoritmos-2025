# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos 
# entre cero y un número entero positivo dado.

def suma(n: int):
    if n <= 0:
        return 0
    else:
        return (n + suma(n - 1))
    
print (suma(5))