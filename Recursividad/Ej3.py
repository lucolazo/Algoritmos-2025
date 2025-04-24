# 3. Implementar una función para calcular el producto de dos números enteros dados.

num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese otro numero: "))

def producto(n1, n2):
    if n1 == 0 or n2 == 0:      # Caso base
        return 0
    if n2 > 0:
        return (n1 + (producto(n1, n2 - 1)))        # Caso recursivo para número positivo: suma n1 con el resultado de la función disminuyendo n2
    else:
        return (-producto(n1, -n2))     # Caso recursivo para número negativo: usamos el negativo del producto con el valor absoluto de n2
    
print(producto(num1, num2))