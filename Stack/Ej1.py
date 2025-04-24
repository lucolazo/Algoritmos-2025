# 1- Determinar el número de ocurrencias de un determinado elemento en una pila.

pila = [2, 4, 6, 8, 4]
valor = 6

def ocurrencias (p, v) -> int:
    aux= []
    contador = 0

    #Recorremos la pila y contamos
    while p:     # "Mientras la pila no esté vacía"
        elemento = p.pop()
        if elemento == v:
            contador += 1
            aux.append(elemento)   # Agregamos el elemento que sacamos a la pila auxiliar

    # Restaurar la pila original
    while aux:
        p.append(aux.pop())

    return contador

print(f"Número de ocurrencias de {valor} es: ", ocurrencias(pila, valor))