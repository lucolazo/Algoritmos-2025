# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
#     a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi
#     dor, router, switch, impresora;
#     b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
#     Red Hat, Debian, Arch;
#     c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
#     Red Hat, Fedora hasta la impresora;
#     d. encontrar el árbol de expansión mínima;
#     e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”
#     f. indicar desde que computadora del switch 01 es el camino más corto
#     al servidor “MongoDB”
#     g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
#     h. debe utilizar un grafo no dirigido.

from graph import Graph

# --- a. Crear grafo no dirigido ---
g = Graph(is_directed=False)

computadoras = {
    "Impresora": "Impresora",
    "Mint": "PC",
    "Ubuntu": "PC",
    "Switch 1": "Switch",
    "Debian": "Notebook",
    "Router 1": "Router",
    "Router 2": "Router",
    "Red Hat": "Notebook",
    "Guaraní": "Servidor",
    "Router 3": "Router",
    "Switch 2": "Switch",
    "Manjaro": "PC",
    "Fedora": "PC",
    "Parrot": "PC",
    "Arch": "Notebook",
    "MongoDB": "Servidor"
}

for nombre, tipo in computadoras.items():
    g.insert_vertex(nombre, other_values={"tipo": tipo})

g.show()

# --- b. Barrido en profundidad y amplitud desde Red Hat, Debian, Arch ---
print("\nBarrido en profundidad desde 'Red Hat':")
g.deep_sweep("Red Hat")
print("\nBarrido en profundidad desde 'Debian':")
g.deep_sweep("Debian")
print("\nBarrido en profundidad desde 'Arch':")
g.deep_sweep("Arch")

print("\nBarrido en amplitud desde 'Red Hat':")
g.amplitude_sweep("Red Hat")
print("\nBarrido en amplitud desde 'Debian':")
g.amplitude_sweep("Debian")
print("\nBarrido en amplitud desde 'Arch':")
g.amplitude_sweep("Arch")

# --- c. Camino más corto Manjaro, Red Hat, Fedora hasta Impresora ---
stack_resultado = g.dijkstra("Manjaro")
print("\nCamino más corto desde 'Manjaro' hasta 'Impresora':")
while not stack_resultado.is_empty():
    print(stack_resultado.pop())

stack_resultado = g.dijkstra("Red Hat")
print("\nCamino más corto desde 'Red Hat' hasta 'Impresora':")
while not stack_resultado.is_empty():
    print(stack_resultado.pop())

stack_resultado = g.dijkstra("Fedora")
print("\nCamino más corto desde 'Fedora' hasta 'Impresora':")
while not stack_resultado.is_empty():
    print(stack_resultado.pop())

# --- d. Árbol de expansión mínima ---
mst = g.kruskal("Router 1")
print("\nÁrbol de expansión mínima (Kruskal):\n", mst)

# --- e. Camino más corto desde PC (no notebook) hasta servidor "Guaraní" ---
pc_no_notebook = [v for v in computadoras if computadoras[v] == "PC"]
caminos_mas_cortos = {}
for pc in pc_no_notebook:
    stack_resultado = g.dijkstra(pc)
    caminos_mas_cortos[pc] = []
    while not stack_resultado.is_empty():
        caminos_mas_cortos[pc].append(stack_resultado.pop())
print("\nCaminos más cortos desde PC (no notebook) hasta 'Guaraní':")
for pc, camino in caminos_mas_cortos.items():
    print(f"Desde {pc}: {camino}")

# --- f. Camino más corto desde computadora del switch 01 hasta servidor "MongoDB" ---
computadoras_switch_01 = ["Mint", "Ubuntu", "Debian", "Red Hat"]
caminos_mas_cortos_switch = {}
for comp in computadoras_switch_01:
    stack_resultado = g.dijkstra(comp)
    caminos_mas_cortos_switch[comp] = []
    while not stack_resultado.is_empty():
        caminos_mas_cortos_switch[comp].append(stack_resultado.pop())
print("\nCaminos más cortos desde computadoras del switch 01 hasta 'MongoDB':")
for comp, camino in caminos_mas_cortos_switch.items():
    print(f"Desde {comp}: {camino}")

# --- g. Cambiar conexión de impresora al router 02 y resolver punto b ---
g.delete_edge("Impresora", "Router 1")
g.insert_edge("Impresora", "Router 2", 4)
print("\nBarrido en profundidad desde 'Red Hat' después de cambiar conexión de impresora:")
g.deep_sweep("Red Hat")
print("\nBarrido en amplitud desde 'Red Hat' después de cambiar conexión de impresora:")
g.amplitude_sweep("Red Hat")
