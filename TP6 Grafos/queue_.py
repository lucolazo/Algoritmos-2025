# typing: Se usa para dar pistas de tipo (type hints).

# Any: Significa que puede recibir cualquier tipo de dato.

# Optional: Indica que puede devolver un valor del tipo indicado o None.

from typing import Any, Optional

class Queue:

    def __init__(self):        # Método constructor.
        self.__elements = []   # Crea una lista privada llamada __elements para almacenar los elementos de la cola.

    def arrive(self, value: Any) -> None:   # Agrega un nuevo elemento al final de la cola.
        self.__elements.append(value)       # Usa append() que pone el valor al final de la lista.

    def attention(self) -> Optional[Any]:   # Atiende (quita) al primer elemento de la cola (el que llegó primero).
        if self.__elements:
            return self.__elements.pop(0)   # pop(0) elimina y devuelve el primer elemento.
        else:
            return None     # Si la cola está vacía, devuelve None.

    def size(self) -> int:
        return len(self.__elements)     # Devuelve la cantidad de elementos que hay en la cola.

    def on_front(self) -> Optional[Any]:
        if self.__elements:
            return self.__elements[0]       # Muestra (sin eliminar) el primer elemento de la cola.
        else:
            return None     # Si la cola está vacía, devuelve None.

    def move_to_end(self) -> Optional[Any]:     # Mueve el primer elemento de la cola al final.
        if self.__elements:
            value = self.attention()        # Usa attention() para quitar el primero.
            self.arrive(value)      # Luego lo agrega de nuevo al final con arrive().
            return value

    def show(self):     # Muestra todos los elementos de la cola, uno por uno.
        for _ in range(len(self.__elements)):       # Los va rotando (cada uno pasa del frente al final), así que la cola no cambia de orden total, pero se recorre entera.
            print(self.move_to_end())       # Usa move_to_end() tantas veces como elementos haya.

q = Queue()  # Crea un objeto de la clase
