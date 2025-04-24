# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

lista= [1, 2, 3, 4, 5]

def secuencia (lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + secuencia(lista[:-1])

print(secuencia(lista))