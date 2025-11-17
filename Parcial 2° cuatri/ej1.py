# Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria
# (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a
# tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual
# debemos construir tres árboles para acceder de manera eficiente a los datos contemplando
# lo siguiente:
# a. los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último,
# la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los
# Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# c. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero
# y eléctrico;
# d. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un
# listado por nivel por nombre;
# e. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# f. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# g. determinar cuantos Pokémons tienen megaevolucion.
# h. determinar cuantos Pokémons tiene forma gigamax.

from tree import BinaryTree
from pokemon_list import pokemon_data

# a. Árboles por nombre, número y tipo
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for p in pokemon_data:
    info = {
        "nombre": p["nombre"],
        "tipo": p["tipo"],
        "debilidades": p["debilidades"],
        "tiene_mega": p["tiene_mega"],
        "tiene_gigamax": p["tiene_gigamax"],
        "numero": p["numero"]
    }

    arbol_nombre.insert(p["nombre"], info)
    arbol_numero.insert(p["numero"], info)
    for t in p["tipo"]:
        arbol_tipo.insert(t, {
            "nombre": p["nombre"],
            "numero": p["numero"],
            "tipos": p["tipo"],
            "debilidades": p["debilidades"],
            "tiene_mega": p["tiene_mega"],
            "tiene_gigamax": p["tiene_gigamax"]
        })

# b. mostrar todos los datos de un Pokémon a partir de su número y nombre
print("\n----- Búsqueda por número -----")
def mostrar_por_numero(num):
    nodo = arbol_numero.search(num)
    if nodo is not None:
        print("Nombre:", nodo.other_values["nombre"])
        print("Número:", num)
        print("Tipos:", nodo.other_values["tipo"])
        print("Debilidades:", nodo.other_values["debilidades"])
        print("Mega:", nodo.other_values["tiene_mega"])
        print("Gigamax:", nodo.other_values["tiene_gigamax"])
    else:
        print("No encontrado")

mostrar_por_numero(25)  # Ejemplo con Pikachu
print()
mostrar_por_numero(130) # Ejemplo con Gyarados
print()
mostrar_por_numero(9999) # Ejemplo no encontrado

print("\n----- Búsqueda de nombre por proximidad -----")
def buscar_por_nombre(prefijo):
    resultados = arbol_nombre.proximity_search(prefijo)
    for r in resultados:
        print(r.value, r.other_values)
    if not resultados:
        print("No encontrado")

buscar_por_nombre("char")  # Ejemplo con Charizard
print()
buscar_por_nombre("xyz")   # Ejemplo sin resultados

# c. Mostrar Pokémon de un tipo
def pokemons_por_tipo(tipo):
    print(f"\n--- Pokémons del tipo {tipo} ---")

    nodo = arbol_tipo.search(tipo)
    if nodo is None:
        print("No hay pokémon de este tipo.")
        return

    def _listar(root):
        if root:
            _listar(root.left)
            print(root.other_values["nombre"])
            _listar(root.right)

    _listar(nodo)

pokemons_por_tipo("Fuego")
pokemons_por_tipo("Eléctrico")

# d. Listados ordenados
print("\n--- Pokémon ordenados por número ---")
arbol_numero.in_order()

print("\n--- Pokémon ordenados por nombre ---")
arbol_nombre.in_order()

print("\n--- Pokémon por niveles (nombre) ---")
arbol_nombre.by_level()

# e. Pokémon débiles a Jolteon, Lycanroc, Tyrantrum
debilidades_buscar = ["Eléctrico", "Roca", "Dragón"]

def buscar_por_debilidad():
    print("\n--- Pokémon débiles a Jolteon, Lycanroc y Tyrantrum ---")

    def _buscar(root):
        if root:
            _buscar(root.left)

            for d in debilidades_buscar:
                if d in root.other_values["debilidades"]:
                    print(root.value, "es débil a:", d)
                    break

            _buscar(root.right)

    _buscar(arbol_nombre.root)


# f. Contar tipos
print("\n--- Conteo de Pokémon por tipo ---")

conteo = {}

def _contar(root):
    if root:
        _contar(root.left)
        for t in root.other_values["tipo"]:
            if t not in conteo:
                conteo[t] = 0
            conteo[t] += 1
        _contar(root.right)

_contar(arbol_nombre.root)

for tipo, cant in conteo.items():
    print(tipo, ":", cant)


# g. Contar megaevoluciones
def contar_mega():
    def _contar(root):
        if root is None:
            return 0
        return _contar(root.left) + _contar(root.right) + (1 if root.other_values["tiene_mega"] else 0)

    print("\nCantidad con megaevolución:", _contar(arbol_nombre.root))

contar_mega()

# h. Contar gigamax
def contar_gigamax():
    def _contar(root):
        if root is None:
            return 0
        return _contar(root.left) + _contar(root.right) + (1 if root.other_values["tiene_gigamax"] else 0)

    print("\nCantidad con forma Gigamax:", _contar(arbol_nombre.root))

contar_gigamax()
