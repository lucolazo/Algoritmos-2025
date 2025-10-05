# a. listado inorder de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree
from criaturas_data import criaturas

criaturas_tree = BinaryTree()

class Criatura: # Para info del other_values
    def __init__(self, derrotada_por, descripcion, capturada_por):
        self.derrotada_por = derrotada_por
        self.descripcion = descripcion
        self.capturada_por = capturada_por

    def __str__(self):
        return f'- Derrotada por: {self.derrotada_por} - Descripción: {self.descripcion} - Capturada por: {self.capturada_por}'

for criatura in criaturas:
    c = Criatura(criatura['Derrotada_por'], criatura['Descripcion'], criatura['Capturada_por'])
    criaturas_tree.insert(criatura['Nombre'], c)    # (value, other_values)

# a. listado inorder de las criaturas y quienes la derrotaron;
print('\n---- Criaturas y sus derrotas inorder ----')
def inorder_criat_derrotas(tree):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            print(f"{root.value} - Derrotada por: {root.other_values.derrotada_por}")
            __rec(root.right)
    __rec(tree.root)

inorder_criat_derrotas(criaturas_tree)

# c. mostrar toda la información de la criatura Talos;
def info_talos(tree):
    nodo = tree.search("Talos")
    if nodo is not None:
        print(f"\nInformación de Talos:\n{nodo.value} {nodo.other_values}")
    else:
        print("\nNo se ha encontrado a Talos en el árbol")

info_talos(criaturas_tree)

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def top3_derrotadores(tree):
    conteo = {} # Creamos un diccionario

    def __rec(root):
        if root is not None:
            __rec(root.left)
            derrotador = root.other_values.derrotada_por    # Guardamos el héroe/dios
            if derrotador is not None:
                conteo[derrotador] = conteo.get(derrotador, 0) + 1  # obtiene el valor actual del héroe y le suma 1
            __rec(root.right)

    __rec(tree.root)

    # sorted((nombre, cantidad), ordenar por cantidad, descendente, tomar los 3 primeros)
    top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    # sorted(): ordena una lista (o iterable) y devuelve una nueva lista ordenada.
    # conteo.items(): convierte el diccionario en una lista de tuplas
    # x: para referirse a una tupla. x[0] sería el nombre, y x[1] la cantidad.
    # reverse=True: cambia el orden a descendente (de mayor a menor).

    print("\n---- Top 3 héroes/dioses que derrotaron más criaturas ----")
    for nombre, cantidad in top3:
        print(f"{nombre}: {cantidad} criaturas derrotadas")

top3_derrotadores(criaturas_tree)

# e. listar las criaturas derrotadas por Heracles;
def derrotadas_heracles(tree):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.derrotada_por == 'Heracles':
                print(root.value)
            __rec(root.right)
    __rec(tree.root)

print('\n---- Criaturas derrotadas por Heracles ----')
derrotadas_heracles(criaturas_tree)

# f. listar las criaturas que no han sido derrotadas;
def criaturas_invictas(tree):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.derrotada_por is None:
                print(root.value)
            __rec(root.right)
    __rec(tree.root)

print('\n---- Criaturas invictas ----')
criaturas_invictas(criaturas_tree)

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
def modificar_captura(tree, criat):
    nodo = tree.search(criat)
    if nodo is not None:
        nodo.other_values.capturada_por = 'Heracles'
        print(f"\n{criat} ahora está capturada por Heracles")
    else:
        print(f"\nNo se ha encontrado a {criat} en el árbol")

modificar_captura(criaturas_tree, "Cerbero")
modificar_captura(criaturas_tree, "Toro de Creta")
modificar_captura(criaturas_tree, "Cierva Cerinea")
modificar_captura(criaturas_tree, "Jabalí de Erimanto")

# i. se debe permitir búsquedas por coincidencia;
print('\n---- Búsquedas por proximidad ----')
criaturas_tree.proximity_search("Es")
criaturas_tree.proximity_search('Jaba')

# j. eliminar al Basilisco y a las Sirenas;
criaturas_tree.delete('Basilisco')
criaturas_tree.delete('Sirenas')
print('\nSe han eliminado Basilisco y Sirenas del árbol')

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
nodo = criaturas_tree.search('Aves del Estínfalo')
if nodo is not None:
    nodo.other_values.derrotada_por = 'Heracles'
    print('\nSe ha modificado la información de las Aves del Estínfalo:')
    print(nodo.value, nodo.other_values)

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
nodo = criaturas_tree.search('Ladón')
if nodo is not None:
    other = nodo.other_values       # guardamos other_values
    criaturas_tree.delete('Ladón')  # eliminamos el nodo viejo
    criaturas_tree.insert('Dragón Ladón', other)  # insertamos con el nuevo nombre

print('\nSe ha modificado el nombre de Ladón por Dragón Ladón:')
print('Dragón Ladón', other)

# m. realizar un listado por nivel del árbol;
print('\n---- Listado por nivel del árbol ----')
criaturas_tree.by_level()

# n. muestre las criaturas capturadas por Heracles.
def capturadas_heracles(tree):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.other_values.capturada_por == 'Heracles':
                print(root.value)
            __rec(root.right)
    __rec(tree.root)

print('\n---- Criaturas capturadas por Heracles ----')
capturadas_heracles(criaturas_tree)
