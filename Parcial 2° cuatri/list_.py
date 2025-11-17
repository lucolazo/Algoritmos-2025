from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(      # Agregar un criterio de ordenamiento o búsqueda
        self,
        key_criterion: str,     # (Nombre del criterio)
        function,       # (Función que recibe un elemento de la lista y devuelve el valor por el cual se lo va a ordenar/buscar.)
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(       # Muestra todos los elementos de la lista, uno por uno.
        self
    ) -> None:
        for element in self:
            print(element)

    def delete_value(       # Busca un valor en la lista y lo elimina si lo encuentra (no sirve para valores repetidos, sólo únicos)
        self,
        value,      # (Valor a buscar)
        key_value: str = None,      # (Criterio opcional para buscar el valor)
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def insert_value(
        self,
        value: Any,
    ) -> None:
        self.append(value)
        # list_number.insert(i, numero)
        # pass

# la función sort() de Python, por defecto, siempre ordena en forma ascendente.
    def sort_by_criterion(      # Ordena la lista según un criterio dado
        self,
        criterion_key: str = None,      # (Nombre del criterio registrado con add_criterion())
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(     # Realiza una búsqueda binaria del valor dado
        self,
        search_value,       # (Valor que se quiere buscar)
        search_key: str = None,     # (Criterio opcional por el que se quiere buscar)
    ) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2
