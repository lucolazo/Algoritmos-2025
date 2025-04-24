# Reemplazar todas las ocurrencias de un determinado elemento en una pila.

pila = [1, 0, 1, 0, 1]

def reemplazar (pila, viejo, nuevo):
    aux = []

    while pila:
        elemento = pila.pop()
        if elemento == viejo:
            aux.append(nuevo)
        else:
            aux.append(elemento)

    while aux:
        pila.append(aux.pop())

    return(pila)

print("Pila original: ", pila)
print("Pila modificada: ", reemplazar(pila, 1, 2))