# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las
# siguientes tareas:
#     a. cada vértice representa un ambiente de una casa: cocina, comedor, cochera, quincho,
#     baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#     b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la
#     arista es la distancia entre los ambientes, se debe cargar en metros;
#     c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#     para conectar todos los ambientes;
#     d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#     determinar cuántos metros de cable de red se necesitan para conectar el router con el
#     Smart Tv.

from graph import Graph

# --- a. Crear grafo no dirigido ---
g = Graph(is_directed=False)

ambientes = [
    "cocina", "comedor", "cochera", "quincho",
    "baño 1", "baño 2", "habitación 1", "habitación 2",
    "sala de estar", "terraza", "patio"
]

for a in ambientes:
    g.insert_vertex(a)

# --- b. Insertar aristas (mínimo 3 por vértice, 2 con 5 conexiones) ---

# Cocina (5)
g.insert_edge("cocina", "comedor", 4)
g.insert_edge("cocina", "baño 1", 6)
g.insert_edge("cocina", "patio", 8)
g.insert_edge("cocina", "habitación 1", 10)
g.insert_edge("cocina", "sala de estar", 7)

# Sala de estar (5)
g.insert_edge("sala de estar", "comedor", 3)
g.insert_edge("sala de estar", "terraza", 9)
g.insert_edge("sala de estar", "patio", 5)
g.insert_edge("sala de estar", "habitación 2", 12)
g.insert_edge("sala de estar", "quincho", 14)

# Otras (mínimo 3)
g.insert_edge("comedor", "baño 1", 5)
g.insert_edge("comedor", "habitación 1", 9)
g.insert_edge("comedor", "patio", 7)

g.insert_edge("cochera", "quincho", 6)
g.insert_edge("cochera", "patio", 11)
g.insert_edge("cochera", "terraza", 13)

g.insert_edge("quincho", "patio", 4)
g.insert_edge("quincho", "terraza", 10)
g.insert_edge("quincho", "baño 2", 9)

g.insert_edge("baño 1", "baño 2", 3)
g.insert_edge("baño 1", "habitación 1", 8)
g.insert_edge("baño 1", "patio", 10)

g.insert_edge("baño 2", "habitación 2", 4)
g.insert_edge("baño 2", "terraza", 7)
g.insert_edge("baño 2", "patio", 6)

g.insert_edge("habitación 1", "habitación 2", 5)
g.insert_edge("habitación 1", "patio", 9)

g.insert_edge("habitación 2", "terraza", 8)
g.insert_edge("habitación 2", "patio", 6)

g.insert_edge("terraza", "patio", 5)


# --- c. MST ---

mst = g.kruskal("cocina")
print("\nÁrbol de expansión mínima (Kruskal):\n", mst)


# sumar metros del MST
def sumar_metros_mst(mst):
    total = 0
    partes = mst.split(";")

    for p in partes:
        piezas = p.split("-")
        # el formato siempre termina en "-peso"
        peso = piezas[-1]
        total += int(peso)

    return total


metros = sumar_metros_mst(mst)
print("\nMetros totales necesarios:", metros)


# --- d. Camino más corto habitación 1 → sala ---

stack_resultado = g.dijkstra("habitación 1")

padres = {}
dist_final = None

while stack_resultado.size() > 0:
    nodo, dist, padre = stack_resultado.pop()
    padres[nodo] = padre
    if nodo == "sala de estar":
        dist_final = dist

print("\nDistancia más corta habitación 1 → sala de estar:", dist_final)

# reconstruir camino
camino = []
actual = "sala de estar"

while actual is not None:
    camino.append(actual)
    actual = padres.get(actual)

camino.reverse()

print("\nCamino más corto:", " → ".join(camino))
