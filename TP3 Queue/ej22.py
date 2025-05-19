# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F)
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from queue_ import Queue

queue = Queue()

# Llenamos la cola
def personajes(nom_per, nom_super, genero):
    personaje = {
        "Nombre del personaje": nom_per,
        "Nombre del superheroe": nom_super,
        "Genero": genero
    }
    queue.arrive(personaje)

personajes("Tony Stark", "Iron Man", "M")
personajes("Natasha Romanoff", "Black Widow", "F")
personajes("Steve Rogers", "Capitán América", "M")
personajes("Bruce Banner", "Hulk", "M")
personajes("Carol Danvers", "Captain Marvel", "F")
personajes("Peter Parker", "Spider-Man", "M")
personajes("Scott Lang", "Ant-Man", "M")
personajes("Wanda Maximoff", "Scarlet Witch", "F")
personajes("T'Challa", "Black Panther", "M")
personajes("Stephen Strange", "Doctor Strange", "M")

#  a. determinar el nombre del personaje de la superhéroe Capitana Marvel
def nombre_personaje(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Nombre del superheroe"] == "Captain Marvel":
            print(elemento["Nombre del personaje"])
        q.arrive(elemento)

    return q

#  b. mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Genero"] == "F":
            print(elemento["Nombre del superheroe"])
        q.arrive(elemento)

    return q

#  c. mostrar los nombres de los personajes masculinos
def personajes_masculinos(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Genero"] == "M":
            print(elemento["Nombre del personaje"])
        q.arrive(elemento)

    return q

#  d. determinar el nombre del superhéroe del personaje Scott Lang
def nombre_superheroe(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Nombre del personaje"] == "Scott Lang":
            print(elemento["Nombre del superheroe"])
        q.arrive(elemento)

    return q

#  e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S
def nombres_con_s(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Nombre del personaje"][0] == "S" or elemento["Nombre del superheroe"][0] == "S":
            print(elemento)
        q.arrive(elemento)

    return q

#  f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre 
# de superhéroes
def determinar_personaje(q):
    contador = 0

    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Nombre del personaje"] == "Carol Danvers":
            print(elemento["Nombre del superheroe"])
            contador += 1
        q.arrive(elemento)

    if contador < 1:
        print("Carol Danvers no se encuentra en la cola")

    return q

print("Nombre del personaje de la superhéroe Capitana Marvel: ")
nombre_personaje(queue)
print()

print("---- Nombres de los superhéroes femeninos ----")
superheroes_femeninos(queue)
print()

print("---- Nombres de los personajes masculinos ----")
personajes_masculinos(queue)
print()

print("Nombre del superhéroe del personaje Scott Lang: ")
nombre_superheroe(queue)
print()

print("---- Datos de los superhéroes o personaje cuyos nombres comienzan con la letra S ----")
nombres_con_s(queue)
print()

print("Nombre de superheroe de Carol Danvers: ")
determinar_personaje(queue)
