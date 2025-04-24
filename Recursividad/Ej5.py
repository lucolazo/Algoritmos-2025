# 5. Desarrollar una función que permita convertir un número romano en un número decimal.

romano = {     # Diccionario de números romanos
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def decimal(n: str) -> int:        #Recibe números romanos (str) y devuelve decimales (int)
    if len(n) == 1:     #Caso base
        return romano[n]
    if romano[n[0]] < romano[n[1]]:     #Comparamos izquierda con derecha
        # Resta
        return -romano[n[0]] + decimal(n[1:])           # '1:' para la cadena sin la primera letra
    else:
        # Suma
        return romano[n[0]] + decimal(n[1:])

print(decimal('XV'))