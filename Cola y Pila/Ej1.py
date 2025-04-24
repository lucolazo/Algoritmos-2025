# 1- Eliminar de una cola de caracteres todas las vocales que aparecen.

from random import randint
from queue_ import Queue

queue_letters = Queue()     # Crea una cola vacía para almacenar letras mayúsculas.

for i in range(15):
    queue_letters.arrive(chr(randint(65, 90)))      # randint(65, 90) genera un número entre 65 y 90 (que son letras de la A a la Z en ASCII).
# chr(...) convierte ese número en una letra.
# arrive(...) agrega esa letra a la cola.

queue_letters.show()        # Muestra las letras generadas antes de eliminar las vocales.
print()

for i in range(queue_letters.size()):       # devuelve cuántos elementos tiene originalmente la cola.
    if queue_letters.on_front() in ["A", "E", "I", "O", "U"]:       # Mira la primera letra sin sacarla. Si está en la lista... 
        queue_letters.attention()       # La elimina.
    else:
        queue_letters.move_to_end()     # La mueve al final (así no se pierde, pero tampoco se evalúa otra vez en el mismo ciclo).

print()
queue_letters.show()        # Muestra el contenido de la cola después de eliminar todas las vocales.