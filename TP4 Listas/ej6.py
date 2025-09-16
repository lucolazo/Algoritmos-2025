# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa
# rias para poder realizar las siguientes actividades:
#  a. eliminar el nodo que contiene la información de Linterna Verde;
#  b. mostrar el año de aparición de Wolverine;
#  c. cambiar la casa de Dr. Strange a Marvel;
#  d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
#  e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
#  f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#  g. mostrar toda la información de Flash y Star-Lord;
#  h. listar los superhéroes que comienzan con la letra B, M y S;
#  i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List
from super_heroes_data import superheroes

class Superhero:

    # Define la estructura del objeto superhéroe.
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    # El método __str__ sirve para que, al imprimir el objeto, se muestre en formato:
    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"


# Ordenamos a los superhéroes por nombre
def order_by_name(item):
    return item.name

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)

# Llenamos la lista
for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

#  a. eliminar el nodo que contiene la información de Linterna Verde;
list_superhero.delete_value('Linterna verde', 'name')
print("\nSe ha eliminado a Linterna Verde.")

# b. mostrar año aparicion wolverine
index = list_superhero.search('Wolverine', 'name')  # Posición
if index:
    print(f'\nAño de aparición de Wolverine: {list_superhero[index].first_appearance}')
else:
    print('\nEl superhéroe no está en la lista')

# c. modificar Dr. Strange de villano a héroe
index = list_superhero.search('Dr Strange', 'name')
if index:
    print(f"\nDr. Strange casa: {list_superhero[index].is_villain}")
    list_superhero[index].is_villain = False
    print(f"Dr. Strange casa: {list_superhero[index].is_villain}")
else:
    print('\nEl superhéroe no está en la lista')

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”
print('\n---- Superhéroes con "traje" o "armadura" en su short_bio ----')
print()
for superhero in list_superhero:
    if 'armor' in superhero.short_bio or 'suit' in superhero.short_bio:
        print(superhero)

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963
print('\n---- Superhéroes con fecha de aparición anterior a 1963 ----')
print()
encontrado = False
for superhero in list_superhero:
    if superhero.first_appearance < 1963:
        print(f"Nombre: {superhero.name}. Casa: {superhero.is_villain}")
        encontrado = True
if not encontrado:
    print('No se encontraron superhéroes con año de aparición previas a 1963')

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print('\n---- Casa de Capitana Marvel y Mujer Maravilla ----')
encontrado = False
for superhero in list_superhero:
    if superhero.name == 'Captain Marvel' or superhero.name == 'Wonder Woman':
        encontrado = True
        print(f"{superhero.name} - Casa: {superhero.is_villain}")
if not encontrado:
    print('No se encontraron superhéroes con esos nombres')

# g. mostrar toda la información de Flash y Star-Lord;
print('\n---- Info Flash y Star-Lord ----')
for superhero in list_superhero:
    if superhero.name == 'The Flash' or superhero.name == 'Star-Lord':
        print(superhero)

# h. listar los superhéroes que comienzan con la letra B, M y S;
print('\n---- Superhéroes que comienzan con B, M y S')
print()
for superhero in list_superhero:
    if superhero.name.startswith(('B', 'M', 'S')):
        print(superhero)

#  i. determinar cuántos superhéroes hay de cada casa de comic. (c son villanos y c héroes)
print('\n---- Cantidad de superhéroes por casa ----')
villains = 0
heroes = 0
for superhero in list_superhero:
    if superhero.is_villain:
        villains += 1
    else:
        heroes += 1
print(f"Villanos: {villains}, Héroes: {heroes}")
