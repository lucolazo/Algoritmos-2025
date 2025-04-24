# Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

from random import randint
from queue_ import Queue

def es_primo(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):     # si un número tiene algún divisor (distinto de 1 y de sí mismo), uno de esos divisores será menor o igual a su raíz cuadrada.
        if n % j == 0:
            return False
    return True

queue_primos = Queue()

for i in range(4):
    queue_primos.arrive(randint(1, 100))

print("Cola original: ")
queue_primos.show()

for i in range(queue_primos.size()):
    num = queue_primos.on_front()
    if not es_primo(num):
        queue_primos.attention()
    else:
        queue_primos.move_to_end()

print()
print("Cola sólo con números primos: ")
queue_primos.show()