# Determinar si una cadena de caracteres es un palíndromo.

pila = ['o', 's', 'o']

def palindromo(pila):
    aux = []        # Creamos ina pila auxiliar

    for elemento in reversed(pila):   # Pasar elementos invertidos
        aux.append(elemento)
        
    if pila == aux:     # Comparamos pila original con la auxiliar
        return("Es un palíndromo.")
    else:
        return("No es un palíndromo.")
    
print(palindromo(pila))
