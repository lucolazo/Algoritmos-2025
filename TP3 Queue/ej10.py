# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, 
# resolver las siguientes actividades:

from queue_ import Queue

queue = Queue()

# Llenamos la pila
def notificaciones(hora, aplicacion, mensaje):
    notificacion = {
        "Hora": hora,
        "Aplicacion": aplicacion,
        "Mensaje": mensaje
    }
    queue.arrive(notificacion)

notificaciones("12:00", "Twitter", "Python")
notificaciones("20:00", "Facebook", "Juan te ha enviado una solicitud de amistad")
notificaciones("15:00", "Google Fotos", "Te has quedado sin espacio de almacenamiento")
notificaciones("08:00", "Twitter", "Juan le ha dado me gusta a tu tweet")
notificaciones("14:00", "Facebook", "Melina te ha enviado un mensaje")
notificaciones("18:00", "Twitter", "Python")
notificaciones("13:00", "Classroom", "Tienes una tarea pendiente de Algoritmos y Bases de Datos")

#  a. escribir una función que elimine de la cola todas las notificaciones de Facebook
def eliminar_facebook(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Aplicacion"] == "Facebook":
            continue
        else:
            q.arrive(elemento)

    return q

#  b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya 
# la palabra ‘Python’, si perder datos en la cola;
def mostrar_twitter(q):
    for _ in range(q.size()):
        elemento = q.attention()

        if "Python" in elemento["Mensaje"]:
            print(elemento)
        q.arrive(elemento)

    return q

#  c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 
# 11:43 y las 15:57, y determinar cuántas son
def almacenar_notificaciones(q):
    aux_pila = []

    for _ in range(q.size()):
        elemento = q.attention()

        if elemento["Hora"] > "11:43" and elemento["Hora"] < "15:57":
            aux_pila.append(elemento)
        else:
            q.arrive(elemento)

    notificaciones_almacenadas = len(aux_pila)  # Cantidad de notificaciones entre las 11:43 y 15:57

    return notificaciones_almacenadas

print()
print("---- Cola sin notificaciones de Facebook ----")
eliminar_facebook(queue)
queue.show()
print()

print("---- Notificaciones de Twitter cuyo mensaje inlcuye 'Python' ----")
mostrar_twitter(queue)
print()

print("---- Notificaciones producidas entre las 11:43 y las 15:57 ----")
cantidad_almacenadas = almacenar_notificaciones(queue)
print(cantidad_almacenadas)
