# Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se 
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver 
# las siguientes actividades:

from Stack import Stack

stack = Stack()

# Cargamos los trajes
def cargar_traje(modelo, pelicula, estado):
    traje= {
        "Modelo": modelo,
        "Película": pelicula,
        "Estado": estado
    }
    stack.push(traje)

cargar_traje("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "Dañado")     # Se repite
cargar_traje("Mark XLV (45)", "Avengers: Age of Ultron", "Impecable")    # Se repite
cargar_traje("Mark XLV (45)", "Captain America: Civil War", "Impecable")
cargar_traje("Mark XLVI (46)", "Captain America: Civil War", "Dañado")
cargar_traje("Traje de Spider-Man", "Captain America: Civil War", "Impecable")  # Se repite
cargar_traje("Mark XLVII (47)", "Spider-Man: Homecoming", "Impecable")
cargar_traje("Traje de Spider-Man", "Spider-Man: Homecoming", "Impecable")
cargar_traje("Mark L (50)", "Avengers: Infinity War", "Destruido")
cargar_traje("Mark XLIV (Hulkbuster)", "Avengers: Infinity War", "Dañado")
cargar_traje("Mark LXXXV (85)", "Avengers: Endgame", "Destruido")

# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, 
# además mostrar el nombre de dichas películas
def buscar_modelo(s):
    aux = Stack()
    contador = 0
    while s.size() > 0:
        elemento = s.pop()
        if elemento["Modelo"] == "Mark XLIV (Hulkbuster)":      # Si lo encontramos:
            print(elemento["Película"])     # Mostramos
            contador += 1
        aux.push(elemento)      # Guardamos

    if contador < 1:    # Si no lo encontramos
        print("El modelo 'Mark XLIV (Hulkbuster)' no fue utilizado en ninguna película.")

    while aux.size() > 0:
        s.push(aux.pop())       # Pasamos al stack

    return s

# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
def mostrar_danados(s):
    aux = Stack()
    modelos_mostrados = set()       # Set(): para evitar mostrar modelos repetidos (Ej: Hulkbuster)
    while s.size() > 0:
        elemento = s.pop()
        if elemento["Estado"] == "Dañado" and elemento["Modelo"] not in modelos_mostrados:
            print(elemento["Modelo"])
            modelos_mostrados.add(elemento["Modelo"])       # Marcamos como mostrado
        aux.push(elemento)

    while aux.size() > 0:
        s.push(aux.pop())       # Pasamos al stack

    return s

# c. eliminar los modelos de los trajes destruidos mostrando su nombre
def eliminar_destruidos(s):
    aux = Stack()
    while s.size() > 0:
        elemento = s.pop()
        if elemento["Estado"] == "Destruido":
            print(elemento["Modelo"])       # Mostramos pero no guardamos
        else:
            aux.push(elemento)      # Si no, guardamos

    while aux.size() > 0:
        s.push(aux.pop())       # Pasamos todo otra vez al stack

    return s


# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
# repetidos en una misma película
def modelo_repetido(s):
    aux = Stack()
    traje_mostrado = set()
    while s.size() > 0:
        elemento = s.pop()
        if elemento["Modelo"] == "Mark LXXXV (85)" and elemento["Modelo"] not in traje_mostrado:
            print(f"Modelo {elemento["Modelo"]} ya usado en la película.")    # Modelo ya existente en la pila
            traje_mostrado.add(elemento["Modelo"])  # Marcamos como mostrado
        aux.push(elemento)

    if not traje_mostrado:        # (no se encontró ese modelo en la pila)
        cargar_traje("Mark LXXXV (85)", "Avengers: Endgame", "Destruido")        # Se carga

    while aux.size() > 0:
        s.push(aux.pop())       # Pasamos al stack

    return s

# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y 
# “Capitan America: Civil War”def mostrar_trajes_peliculas(s):
def mostrar_trajes_peliculas(s):
    aux = Stack()
    trajes_mostrados = set()
    while s.size() > 0:
        elemento = s.pop()
        if elemento["Película"] in ["Spider-Man: Homecoming", "Captain America: Civil War"] and elemento["Modelo"] not in trajes_mostrados:
            print(elemento["Modelo"])
            trajes_mostrados.add(elemento["Modelo"])
        aux.push(elemento)

    while aux.size() > 0:
        s.push(aux.pop())

    return s

print()
print("---- Películas en las que se utilizó el modelo Mark XLIV (Hulkbuster) ----")
buscar_modelo(stack)

print()
print("---- Modelos que quedaron dañados ----")
mostrar_danados(stack)

print()
print("---- Modelos destruidos eliminados ----")
eliminar_destruidos(stack)

print()
modelo_repetido(stack)

print()
print("---- Modelos usados en 'Spider-Man: Homecoming' y 'Capitan America: Civil War' ----")
mostrar_trajes_peliculas(stack)
