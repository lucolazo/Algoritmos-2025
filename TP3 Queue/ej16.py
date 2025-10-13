# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
#  a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
#  b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#  c. cargue dos documentos del staff de TI.
#  d. cargue un documento del gerente.
#  e. imprima los dos primeros documentos de la cola.
#  f. cargue dos documentos de empleados y uno de gerente.
#  g. imprima todos los documentos de la cola de impresión.

# como el gerente (3) sería la prioridad más alta, uso un heap maximo
from heap import HeapMax

priority_queue = HeapMax()

# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
priority_queue.arrive('doc_empleado_1', 1)
priority_queue.arrive('doc_empleado_2', 1)
priority_queue.arrive('doc_empleado_3', 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print("\n----- Primer documento de la cola -----")
print(priority_queue.attention())

# c. cargue dos documentos del staff de TI.
priority_queue.arrive('doc_ti_1', 2)
priority_queue.arrive('doc_ti_2', 2)

# d. cargue un documento del gerente.
priority_queue.arrive('doc_gerente_1', 3)

# e. imprima los dos primeros documentos de la cola.
print("\n----- Dos primeros documentos de la cola -----")
print(priority_queue.attention())
print(priority_queue.attention())

# f. cargue dos documentos de empleados y uno de gerente.
priority_queue.arrive('doc_empleado_4', 1)
priority_queue.arrive('doc_empleado_5', 1)
priority_queue.arrive('doc_gerente_2', 3)

# g. imprima todos los documentos de la cola de impresión.
print("\n----- Todos los documentos de la cola de impresión -----")
while priority_queue.size() > 0:
    print(priority_queue.attention())
