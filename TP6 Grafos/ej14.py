# 14. Implementar sobre un casa no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

from graph import Graph
import math

casa = Graph(is_directed=False) # casa NO dirigido

def crear_casa(casa):
    #a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
    ambientes = [
        "Cocina",
        "Comedor",
        "Cochera",
        "Quincho",
        "Baño1",
        "Baño2",
        "Habitacion1",
        "Habitacion2",
        "SalaEstar",
        "Terraza",
        "Patio"
    ]

    # Insertar ambientes como vértices
    for amb in ambientes:
        casa.insert_vertex(amb)

    # b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el weight de la arista es la distancia entre los ambientes, se debe cargar en metros;

    conexiones = [
        # Cocina (5)
        ("Cocina", "Comedor", 4),
        ("Cocina", "Patio", 6),
        ("Cocina", "SalaEstar", 7),
        ("Cocina", "Baño1", 5),
        ("Cocina", "Habitacion1", 8),


        # Comedor (5)
        ("Comedor", "SalaEstar", 3),
        ("Comedor", "Patio", 5),
        ("Comedor", "Quincho", 12),
        ("Comedor", "Baño2", 6),
        ("Comedor", "Habitacion2", 9),


        # Cochera (3)
        ("Cochera", "Patio", 10),
        ("Cochera", "Quincho", 14),
        ("Cochera", "Baño1", 11),


        # Quincho (3)
        ("Quincho", "Terraza", 9),
        ("Quincho", "Patio", 7),
        ("Quincho", "Habitacion2", 13),


        # Baño1 (3)
        ("Baño1", "Habitacion1", 4),
        ("Baño1", "SalaEstar", 6),
        ("Baño1", "Baño2", 5),


        # Baño2 (3)
        ("Baño2", "Habitacion2", 5),
        ("Baño2", "SalaEstar", 4),
        ("Baño2", "Terraza", 8),


        # Habitacion1 (3)
        ("Habitacion1", "SalaEstar", 8),
        ("Habitacion1", "Habitacion2", 6),
        ("Habitacion1", "Terraza", 9),


        # Habitacion2 (3)
        ("Habitacion2", "Terraza", 10),
        ("Habitacion2", "Patio", 7),
        ("Habitacion2", "SalaEstar", 6),


        # SalaEstar (3)
        ("SalaEstar", "Terraza", 8),
        ("SalaEstar", "Patio", 5),
        ("SalaEstar", "Quincho", 10),


        # Terraza (3)
        ("Terraza", "Patio", 12),
        ("Terraza", "Quincho", 9),
        ("Terraza", "Cochera", 15),


        # Patio (3)
        ("Patio", "Cocina", 6),
        ("Patio", "Comedor", 5),
        ("Patio", "Habitacion2", 7),
    ]

    for a, b, metros in conexiones:
        casa.insert_edge(a, b, metros)

    return casa


# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
def arbol_expansion_minima_metros(casa, vertice):
    print("ÁRBOL DE EXPANSIÓN MÍNIMA: ")

    expansion_tree = casa.kruskal(vertice)  # origen arbitrario
    total_metros = 0

    for edge in expansion_tree.split(";"):
        origin, destination, weight = edge.split("-")
        weight = int(weight)
        total_metros += weight
        print(f"{origin} -- {destination} ({weight} m)")

    print(f"Total de metros necesarios: {total_metros} m")
    


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
def habitacion1_sala(casa):
    path = casa.dijkstra('Habitacion1') 
    destination = 'SalaEstar'
    peso_total = None
    camino_completo = []
    resultados = {}

    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]

    camino_completo.reverse()

    resultados['Habitacion1'] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }

    return resultados

#MAIN:
casa = crear_casa(casa)
# casa.show()
print()
arbol_expansion_minima_metros(casa,"Cocina") #elijo por ejemplo la cocina
print()
print("El camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv: ")
print(habitacion1_sala(casa))