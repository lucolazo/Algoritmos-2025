# 2- Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden 
# números pares.

pila = [1, 2, 3, 6, 8, 7]

def impares (p):
    aux = []
    while pila:
        elemento = p.pop()
        if elemento % 2 == 0:
            aux.append(elemento)
        
    while aux:
        p.append(aux.pop())

impares(pila)
print("La pila con números pares: ", pila)