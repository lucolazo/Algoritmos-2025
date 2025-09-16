# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie.
#  a. listado ordenado por nombre y por especie;
#  b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
#  c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#  d. mostrar los Jedi de especie humana y twi'lek;
#  e. listar todos los Jedi que comienzan con A;
#  f. mostrar los Jedi que usaron sable de luz de más de un color;
#  g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#  h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from list_ import List

list_jedis = List()

def order_by_nombre(item):
    return item.nombre

def order_by_especie(item):
    return item.especie

list_jedis.add_criterion("Nombre", order_by_nombre)
list_jedis.add_criterion("Especie", order_by_especie)

class Jedi:
    def __init__(self, nombre, maestros, color_sable, especie):
        self.nombre = nombre
        self.maestros = maestros
        self.color_sable = color_sable
        self.especie = especie

    def __str__(self):
        return f"{self.nombre}: {self.maestros} - {self.color_sable} - {self.especie}"

jedis = [
    Jedi("Yoda", [], ["Verde"], "Desconocida"),
    Jedi("Mace Windu", ["Cyslin Myr"], ["Violeta"], "Humano"),
    Jedi("Obi-Wan Kenobi", ["Qui-Gon Jinn", "Yoda"], ["Azul"], "Humano"),
    Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["Azul", "Rojo"], "Humano"),
    Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["Azul", "Verde"], "Humano"),
    Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["Verde", "Azul", "Blanco"], "Togruta"),
    Jedi("Qui-Gon Jinn", ["Dooku"], ["Verde"], "Humano"),
    Jedi("Count Dooku", ["Yoda"], ["Azul", "Rojo"], "Humano"),
    Jedi("Kit Fisto", ["Yoda"], ["Verde"], "Nautolano"),
    Jedi("Rey", ["Luke Skywalker", "Leia Organa"], ["Azul", "Amarillo"], "Humana"),
    Jedi("Aayla Secura", ["Quinlan Vos", "Tholme"], ["Azul"], "Twi'lek")
]

for jedi in jedis:
    list_jedis.insert_value(jedi)

# a. listado ordenado por nombre
list_jedis.sort_by_criterion("Nombre")
print("\n---- Lista ordenada por nombre ----")
list_jedis.show()

# listado ordenado por especie
list_jedis.sort_by_criterion("Especie")
print("\n---- Lista ordenada por especie ----")
list_jedis.show()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
print("\n---- Información de Ahsoka Tano y Kit Fisto ----")
encontrado = False
for jedi in list_jedis:
    if "Ahsoka Tano" in jedi.nombre or "Kit Fisto" in jedi.nombre:
        encontrado = True
        print(jedi)
if not encontrado:
    print("\nNo se han encontrado Jedis con esos nombres.")

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices
print("\n---- Padawan de Yoda y Luke Skywalker ----")
encontrado = False
for jedi in list_jedis:
    if "Yoda" in jedi.maestros or "Luke Skywalker" in jedi.maestros:
        encontrado = True
        print(jedi.nombre)
if not encontrado:
    print("No se han encontrado padawan de Yoda y Luke Skywalker.")

# d. mostrar los Jedi de especie humana y twi'lek;
print("\n---- Jedis de especie humana y twi'lek ----")
encontrado = False
for jedi in list_jedis:
    if "Humano" in jedi.especie or "Twi'lek" in jedi.especie:
        encontrado = True
        print(f"{jedi.nombre} ({jedi.especie})")
if not encontrado:
    print("\nNo se han encontrado jedis de esas especies.")

# e. listar todos los Jedi que comienzan con A
print("\n---- Jedis que comienzan con A ----")
encontrado = False
for jedi in list_jedis:
    if jedi.nombre.startswith("A"):
        encontrado = True
        print(jedi.nombre)
if not encontrado:
    print("No se han encontrado Jedis cuyo nombre comiencen con 'A'")

# f. mostrar los Jedi que usaron sable de luz de más de un color
print("\n---- Jedis que usaron sable de luz de más de un color ----")
encontrado = False
for jedi in list_jedis:
    if len(jedi.color_sable) > 1:
        encontrado = True
        print(jedi.nombre)
if not encontrado:
    print("\nNo se han encontrado Jedis que hayan utilizado sables de más de un color.")

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta
print("\n---- Jedi que utilizaron sable de luz amarillo o violeta ----")
encontrado = False
for jedi in list_jedis:
    if "Amarillo" in jedi.color_sable or "Violeta" in jedi.color_sable:
        encontrado = True
        print(jedi.nombre)
if not encontrado:
    print("No se han encontrado Jedis que hayan utilizado sables amarillos y violetas")

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("\n---- Padawans de Qui-Gon Jin y Mace Windu ----")
encontrado = False
for jedi in list_jedis:
    if "Qui-Gon Jinn" in jedi.maestros or "Mace Windu" in jedi.maestros:
        encontrado = True
        print(jedi.nombre)
if not encontrado:
    print("\nNo se han encontrado Padawans de Qui-Gon Jinn y Mace Windu.")
