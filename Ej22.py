#  22. El problema de la mochila Jedi. Suponga que un Jedi está atrapado, pero muy cerca está su mochila que contiene muchos 
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
# ayuda de la fuerza” realizar las siguientes actividades:
#  a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#  b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#  c. Utilizar un vector para representar la mochila.

mochila = [
    'kit de herramientas',
    'holocron',
    'comunicador',
    'ración de comida',
    'sable de luz',
    'kit médico',
    'holomapa',
    'capa adicional',
    'holopad',
    'reliquia'
]

def usar_la_fuerza(m, contador=0):
    if len(m) == 0:       # Caso base: mochila vacía
        return False, contador

    objeto = m[0]   #Saca el primer objeto de la mochila
    contador += 1       # Empieza a contar

    if objeto == 'sable de luz':
        return True, contador
    else:                          # Si el objeto no es el sable, entonces se llama de nuevo a la función con el resto de la mochila (m[1:], o sea, sin el primer objeto).
        return usar_la_fuerza(m[1:], contador)      # Se pasa también el contador actualizado.
    
#True/False, contador
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Se encontró un sable de luz! Se sacaron: {objetos_sacados} objetos")
else:
    print("No se encontró ningún sable de luz")
