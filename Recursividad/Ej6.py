# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

lista= [1, 2, 3, 4, 5]

def secuencia (l):
    if len(l) == 0:
        return []
    else:
        return [l[-1]] + secuencia(l[:-1])

print(secuencia(lista))