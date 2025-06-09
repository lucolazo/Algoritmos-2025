# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#     funcion recursiva para buscar, determinar si Capitan America esta en la lista.
#     funcion recursiva para listar los superheroes de la lista.

from superheroes_ import superheroes

def buscar_capitan_america(lista):
    if not lista:  # Caso base: lista vacía
        return False
    if lista[0]["name"] == "Captain America":
        return True
    # Se llama a sí misma con la lista exceptuando el primero que ya sacamos
    return buscar_capitan_america(lista[1:])

def listar_superheroes(lista):
    if not lista:   # Caso base: lista vacía
        return False
    print(lista[0]["name"])
    # Se llama a sí misma con la lista exceptuando el primero que ya sacamos
    return listar_superheroes(lista[1:])

# Si está Capitán América o no...
if buscar_capitan_america(superheroes):
    print("Sí se ha encontrado a 'Capitán América' en la lista.")
else:
    print("No se ha encontrado a 'Capitán América' en la lista.")

print()
print("---- Lista de superhéroes ----")
listar_superheroes(superheroes)
