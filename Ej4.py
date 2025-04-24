# 4. Implementar una función para calcular la potencia dado dos números enteros, el primero 
# representa la base y segundo el exponente.

base= int(input("Ingrese la base: "))
exponente = int(input("Ingrese la potencia: "))

def potencia (b, e):
    if e == 0:       # Caso base: cualquier número a la potencia 0 es 1
        return 1
    if e > 0:       # Caso recursivo para exponentes positivos
        return (b * potencia(b, e - 1))
    else:
        return 1/ potencia(b, -e)       # Caso recursivo para exponentes negativos
    
print(potencia(base, exponente))        