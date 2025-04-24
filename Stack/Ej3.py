# Reemplazar todas las ocurrencias de un determinado elemento en una pila.

pila = [1, 0, 1, 0, 1]

def reemplazar (p, viejo, nuevo):
    aux = []

    while p:
        elemento = p.pop()
        if elemento == viejo:
            aux.append(nuevo)
        else:
            aux.append(elemento)

    while aux:
        p.append(aux.pop())

    return(p)

print("Pila original: ", pila)
print("Pila modificada: ", reemplazar(pila, 1, 2))