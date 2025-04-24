# Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

pila = [1, 2, 3, 4, 5]

def invertir(pila):
    aux = []

    while pila:
        aux.append(pila.pop())

    while aux:
        pila.append(aux.pop(0))  #pop() sin argumentos saca del final, pero pop(0) saca del principio
    
    return(pila)

print(invertir(pila))