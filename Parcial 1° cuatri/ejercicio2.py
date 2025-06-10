# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
#     a- Listado ordenado de manera ascendente por nombre de los personajes.
#     b- Determinar en que posicion esta The Thing y Rocket Raccoon.
#     c- Listar todos los villanos de la lista.
#     d- Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
#     e- Listar los superheores que comienzan con  Bl, G, My, y W.
#     f- Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
#     g- Listado de superheroes ordenados por fecha de aparación.
#     h- Modificar el nombre real de Ant Man a Scott Lang.
#     i- Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
#     j- Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from queue_ import Queue
from superheroes_ import superheroes
from list_ import List

def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name or ""

def order_by_first_appearance(item):
    return item.first_appearance

class Superhero:
    # Estructura del superhéroe
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    # Formato para imprimir
    def __str__(self):
        return f"""{self.name}, {self.alias}, {self.real_name} - {self.is_villain} - {self.first_appearance}
{self.short_bio} """

list_superhero = List()

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.insert_value(hero)

# a- Listado ordenado de manera ascendente por nombre de los personajes.
print()
print("---- Lista ordenada por nombre de personajes ----")
list_superhero.add_criterion("name", order_by_name)
list_superhero.sort_by_criterion("name")
for superheroe in list_superhero:
    print(superheroe.name)

# b- Determinar en que posicion esta The Thing y Rocket Raccoon.
pos_thing = list_superhero.search('The Thing', 'name')
pos_rocket = list_superhero.search('Rocket Raccoon', 'name')

print()
print(f"Rocket Raccoon se encuentra en la posición {pos_rocket} de la lista")
print(f"The Thing se encuentra en la posición {pos_thing} de la lista")

# c- Listar todos los villanos de la lista.
print()
print("---- Villanos de la lista ----")
for superheroe in list_superhero:
    if superheroe.is_villain:
        print(superheroe.name)

# d- Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
cola_villanos = Queue()
for superheroe in list_superhero:
    if superheroe.is_villain:
        cola_villanos.arrive(superheroe)

print()
print("---- Villanos que aparecieron antes de 1980 en la cola ----")
for i in range(cola_villanos.size()):
    villano = cola_villanos.on_front()
    if villano.first_appearance < 1980:
        print(villano.name)
    cola_villanos.move_to_end()

# e- Listar los superheores que comienzan con  Bl, G, My, y W.
print()
print("---- Superheores que comienzan con  Bl, G, My, y W ----")
for superheroe in list_superhero:
    if superheroe.name.startswith(("Bl", "G", "My", "W")):
        print(superheroe.name)

# f- Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
list_superhero.add_criterion("real_name", order_by_real_name)
list_superhero.sort_by_criterion("real_name")
print()
print("---- Nombre real de personajes ordenado ----")
for superheroe in list_superhero:
    print(superheroe.real_name)

# g- Listado de superheroes ordenados por fecha de aparación.
list_superhero.add_criterion("first_appearance", order_by_first_appearance)
list_superhero.sort_by_criterion("first_appearance")
print()
print("---- Superheroes ordenados por fecha de aparación ----")
for superheroe in list_superhero:
    print(superheroe.name)

# h- Modificar el nombre real de Ant Man a Scott Lang.
print()
print("---- Modificar el nombre real de Ant Man a Scott Lang ----")
index = list_superhero.search("Ant Man", "name")
if index:
    print(f"Antes: {list_superhero[index].real_name}")
    list_superhero[index].real_name = "Scott Lang"
    print(f"Después: {list_superhero[index].real_name}")
else:
    print("El superhéroe no se encuentra en la lista.")

# i- Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print()
print("---- Personajes que en su biografia incluyan la palabra time-traveling o suit ----")
for superheroe in list_superhero:
    if "time-traveling" in superheroe.short_bio or "suit" in superheroe.short_bio:
        print(superheroe.name)

# j- Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
# Con función para evitar repetir código con c/u
def eliminar_personaje(lista, nombre_personaje):
    encontrado = False
    for s in lista:
        if s.name == nombre_personaje:
            encontrado = True
            print(f"Se ha eliminado a {nombre_personaje}.")
            print(s)
            lista.delete_value(nombre_personaje, "name")
            break
    if not encontrado:
        print(f"No se ha encontrado a {nombre_personaje} en la lista.")
print()
eliminar_personaje(list_superhero, "Electro")
print()
eliminar_personaje(list_superhero, "Baron Zemo")
