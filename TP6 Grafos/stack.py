from typing import Any, Optional

class Stack:

    def __init__(self):   #Constructor
        self.__elements = []

    def push(self, value: Any) -> None:     # Añadir un elemento a la pila (al final)
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:     # Eliminar y retornar el último elemento de la pila
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:      # Obtener el tamaño de la pila (cantidad de elementos)
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:      # Obtener el último elemento SIN eliminarlo
        return (
            self.__elements[-1]
            if self.__elements
            else None
            )

    def is_empty(self):     # o se puede hacer con .size() > 0
        return len(self.__elements) == 0  # True si no hay elementos

    def show(self):     # Mostrar la pila
        print(self.__elements)

stack = Stack()