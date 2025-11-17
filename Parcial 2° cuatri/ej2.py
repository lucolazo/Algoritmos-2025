# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos
# necesarios para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad
# de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar
# todos los pares de personajes que coinciden con dicho número;
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,
# C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# e. calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# f. indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph
from starwars_relations import relations

g = Graph(is_directed=False)

# a. Vértices = personajes
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,
# C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett",
    "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca",
    "Han Solo", "R2-D2", "BB-8"
]

for p in personajes:
    g.insert_vertex(p)

# Aristas = cantidad de episodios compartidos
g.insert_edge("C-3PO", "R2-D2", 9)
g.insert_edge("Luke Skywalker", "Leia", 6)
g.insert_edge("Luke Skywalker", "Darth Vader", 4)
g.insert_edge("Han Solo", "Chewbacca", 7)
g.insert_edge("Rey", "BB-8", 3)
g.insert_edge("Rey", "Kylo Ren", 2)
g.insert_edge("Darth Vader", "Leia", 2)
g.insert_edge("Luke Skywalker", "R2-D2", 6)
g.insert_edge("C-3PO", "Luke Skywalker", 6)

# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia
print("\n--- Árbol de expansión mínimo ---")
print("\nMST desde C-3PO:", g.kruskal("C-3PO"))
print("\nMST desde Yoda:", g.kruskal("Yoda"))
print("\nMST desde Leia:", g.kruskal("Leia"))

# c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar
# todos los pares de personajes que coinciden con dicho número;
print("\n--- Máximo número de episodios compartidos ---")
max_w = -1
pares = set()

for v in g:
    for edge in v.edges:
        a, b = sorted([v.value, edge.value])
        if edge.weight > max_w:
            max_w = edge.weight
            pares = {(a, b)}
        elif edge.weight == max_w:
            pares.add((a, b))

print("Máximo episodios juntos:", max_w)
print("Pares:", pares)

# e. calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
print("\n--- Caminos más cortos ---")
def reconstruir_camino(stack, origen, destino):
    dist = {}
    padre = {}

    # Recuperar los datos del stack que devuelve Dijkstra
    while stack.size() > 0:
        nodo, costo, p = stack.pop()
        dist[nodo] = costo
        padre[nodo] = p

    # Si destino no aparece o su distancia es infinita entonces no hay camino
    if destino not in dist or dist[destino] == float('inf'):
        return None, []   # costo, camino

    # Reconstrucción del camino
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = padre.get(actual)

    camino.reverse()
    return dist[destino], camino

# Ejemplo de C-3PO a R2-D2
stk = g.dijkstra("C-3PO")
costo, camino = reconstruir_camino(stk, "C-3PO", "R2-D2")

print("Camino más corto de C-3PO a R2-D2:", camino, "Costo:", costo)

# Ejemplo de Yoda a Darth Vader
stk = g.dijkstra("Yoda")
costo, camino = reconstruir_camino(stk, "Yoda", "Darth Vader")

print("Camino más corto de Yoda a Darth Vader:", camino, "Costo:", costo)
# f. indicar qué personajes aparecieron en los nueve episodios de la saga.
print("\n--- Personajes en los nueve episodios ---")
episodios = {
    "C-3PO": set(range(1, 10)),
    "R2-D2": set(range(1, 10)),
    "Rey": {7,8,9},
    "Luke Skywalker": {1,2,3,4,5,6}
}

todos = set(range(1, 10))
aparecen_en_9 = [p for p, ep in episodios.items() if ep == todos]

print("Personajes en los 9 episodios:")
print(aparecen_en_9)
