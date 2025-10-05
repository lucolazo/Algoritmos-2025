# Dado un árbol con los nombre de los superhéroes y villanos de la saga MCU.
    # a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
    #   que indica si es un héroe o un villano, True y False respectivamente;
    # b. listar los villanos ordenados alfabéticamente;
    # c. mostrar todos los superhéroes que empiezan con C;
    # d. determinar cuántos superhéroes hay el árbol;
    # e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
    #   encontrarlo en el árbol y modificar su nombre;
    # f. listar los superhéroes ordenados de manera descendente;
    # g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
    #   los villanos, luego:
        # I. determinar cuántos nodos tiene cada árbol;
        # II. realizar un barrido ordenado alfabéticamente de cada árbol

from tree import BinaryTree
from super_heroes_data import superheroes

arbol = BinaryTree()

# a. almacenar nodo con nombre del superhéroe y si es villano o no;
for super_hero in superheroes:
    # Tratamos a is_villain como un diccionario para que no se rompa el other_values
    arbol.insert(super_hero['name'], {'is_villain': super_hero['is_villain']})

# b. listar los villanos ordenados alfabéticamente;
print("\n----- Listado de villanos ordenados alfabéticamente -----")
arbol.villain_in_order()

# c. mostrar todos los superhéroes que empiezan con C;
def show_starts_with_c(tree):
    def __rec(root):
        if root is not None:
            __rec(root.left)
            if root.value.startswith("C"):
                print(root.value)
            __rec(root.right)
    __rec(tree.root)

print("\n----- superhéroes que empiezan con C -----")
show_starts_with_c(arbol)

# d. determinar cuántos superhéroes hay el árbol
print(f"\nCantidad de superhéroes del árbol: {arbol.count_heroes()}")

# e. Búsqueda por proximidad para encontrar a Dr Strange en el árbol y modificar su nombre;
print("\n----- Modificar nombre de Dr Strange -----")
def modificar_dr_strange(tree, nuevo_nombre):
    print('Busqueda por proximidad:')
    tree.proximity_search("Dr Str")
    nodo = tree.search("Dr Strange")
    if nodo is not None:
        other = nodo.other_values       # guardamos other_values
        tree.delete("Dr Strange")       # eliminamos el nodo viejo
        tree.insert(nuevo_nombre, other) # insertamos con el nuevo nombre
        print(f"Nombre de Dr Strange modificado a: {nuevo_nombre}")
    else:
        print("No se ha encontrado a Dr Strange en el árbol")

modificar_dr_strange(arbol, "Algoritmos")

# f. listar los superhéroes ordenados de manera descendente;
print("\n----- Superhéroes ordenados de manera descendente -----")
def heroes_desc(tree):
    def __rec(root):
        if root is not None:
            __rec(root.right)
            if not root.other_values["is_villain"]:
                print(root.value)
            __rec(root.left)
    __rec(tree.root)

heroes_desc(arbol)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#   los villanos, luego resolver las siguiente tareas:
villains_tree = BinaryTree()
heroes_tree = BinaryTree()

arbol.divide_tree(heroes_tree, villains_tree)

    # I. determinar cuántos nodos tiene cada árbol;
def cantidad_nodos(tree):
    def __cant(root):
        if root is None:
            return 0
        return 1 + __cant(root.left) + __cant(root.right)
    return __cant(tree.root)

print(f"\nLa cantidad de nodos del árbol de villanos es: {cantidad_nodos(villains_tree)}")
print(f"\nLa cantidad de nodos del árbol de superhéroes es: {cantidad_nodos(heroes_tree)}")

    # II. realizar un barrido ordenado alfabéticamente de cada árbol
print("\n----- Árbol de villanos en órden alfabético -----")
villains_tree.in_order()
print("\n----- Árbol de superhéroes en órden alfabético -----")
heroes_tree.in_order()
