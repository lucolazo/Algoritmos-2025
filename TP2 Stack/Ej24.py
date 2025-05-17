# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
# necesarias para resolver las siguientes actividades:

from Stack import Stack

stack = Stack()

def cargar_personaje(nombre, peliculas):
    personaje = {
        "Nombre": nombre,
        "Películas": peliculas
    }
    stack.push(personaje)

cargar_personaje("Iron man", 9)
cargar_personaje("Captain America", 7)
cargar_personaje("Thor", 8)
cargar_personaje("Black Widow", 8)
cargar_personaje("Thanos", 4)
cargar_personaje("Rocket Raccoon", 7)   # pos 7
cargar_personaje("Hulk", 7)
cargar_personaje("Black Panther", 5)
cargar_personaje("Doctor Strange", 6)
cargar_personaje("Ant-Man", 5)
cargar_personaje("Groot", 7)        # pos 2
cargar_personaje("Spider-Man", 6)       # Cima de la pila (pos: 1)

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
def buscar_posicion(s):
    pos = 1
    pos_groot = 0
    pos_raccoon = 0
    aux = Stack()

    while s.size() > 0:
        elemento = s.pop()
        if elemento["Nombre"] == "Rocket Raccoon":
            pos_raccoon = pos
            print("Posición de 'Rocket Raccoon' en la pila: ", pos_raccoon)
        if elemento["Nombre"] == "Groot":
            pos_groot = pos
            print("Posición de 'Groot' en la pila: ", pos_groot)
        aux.push(elemento)
        pos += 1

    while aux.size() > 0:
        s.push(aux.pop())       # Pasamos todo al stack

    return s

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece
def personaje_mas_participativo(s):
    aux = Stack()

    while s.size() > 0:
        elemento = s.pop()
        if elemento["Películas"] > 5:
            print(f"{elemento["Nombre"]}: {elemento["Películas"]}")
        aux.push(elemento)

    while aux.size() > 0:
        s.push(aux.pop())

    return s

# c. determinar en cuantas películas participó la Viuda Negra (Black Widow)
def peliculas_blackwidow(s):
    aux = Stack()

    while s.size() > 0:
        elemento = s.pop()
        if elemento["Nombre"] == "Black Widow":
            print(elemento["Películas"])
        aux.push(elemento)

    while aux.size() > 0:
        s.push(aux.pop())

    return s

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
def personajes_iniciales(s):
    aux = Stack()

    while s.size() > 0:
        elemento = s.pop()
        inicial = elemento["Nombre"][0]     # [0]: para acceder a la primer letra
        if inicial in ["C", "D", "G"]:
            print(elemento["Nombre"])
        aux.push(elemento)

    while aux.size() > 0:
        s.push(aux.pop())

    return s

print()
buscar_posicion(stack)

print()
print("---- Personajes que aparecieron en más de 5 películas ----")
personaje_mas_participativo(stack)

print()
print("--- Películas en las que participó Black Widow ----")
peliculas_blackwidow(stack)

print()
print("---- Personajes cuyos nombre empiezan con C, D y G ----")
personajes_iniciales(stack)
