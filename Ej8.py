# 8- Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a 
# sistema binario.

def SistemaBinario(n: int) -> str:
    if n == 1:
        return '1'
    if n == 0:
        return '0'
    return SistemaBinario(n // 2) + str(n % 2)
        
print(SistemaBinario(2))