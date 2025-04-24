# 1- Determinar el número de ocurrencias de un determinado elemento en una pila.

pila = [2, 4, 6, 8, 4]

def ocurrencias (pila, valor) -> int:
    aux= []
    contador = 0

    #Recorremos la pila y contamos
    while pila:     # "Mientras la pila no esté vacía"
        elemento = pila.pop()
        if elemento == valor:
            contador += 1
            aux.append(elemento)   # Agregamos el elemento que sacamos a la pila auxiliar

    # Restaurar la pila original
    while aux:
        pila.append(aux.pop())

    return contador

valor = 6 
print(f"Número de ocurrencias de {valor} es: ", ocurrencias(pila, valor))
