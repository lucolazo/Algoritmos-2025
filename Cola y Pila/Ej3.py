# 3- Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar 
# si es un palíndromo.

from queue_ import Queue

queue_caracteres = Queue()

for valor in ["o", "s", "o"]:       # Llenamos la cola con caracteres
    queue_caracteres.arrive(valor)

print("La cola: ")
queue_caracteres.show()

stack = []      # Creamos una pila y cola auxiliar
queue_aux = Queue()
es_palindroma = True

for i in range(queue_caracteres.size()):        # Transferir de la cola a la pila y a una cola auxiliar (para no perder los datos)
    valor = queue_caracteres.attention()
    stack.append(valor)
    queue_aux.arrive(valor)

while stack:
    if stack.pop() != queue_aux.attention():        # (!=) --> "Distinto de"
        es_palindroma = False
        break       # Se corta directamente si uno ya no coincide

print()
print("Es palíndroma :)" if es_palindroma else "No es palíndroma.")