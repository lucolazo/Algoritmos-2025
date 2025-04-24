# 2- Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from random import randint
from queue_ import Queue

queue_invertida = Queue()   # Creamos una cola vacía

for i in range(5):
    queue_invertida.arrive(randint(1, 100))     # Llenamos la cola con números aleatorios entre 1 y 10

print("Cola original: ")
queue_invertida.show()      # Mostramos la cola sin cambios.
print()

pila = []       # Creamos una pila vacía

for i in range(queue_invertida.size()):      
    pila.append(queue_invertida.attention())        # Pasamos los elementos de la cola a la pila

while pila:
    queue_invertida.arrive(pila.pop())      # saca de la pila (último en entrar, primero en salir) y mete en la cola

print()
print("Cola con los cambios: ")
queue_invertida.show()      # Muestra la cola con los cambios