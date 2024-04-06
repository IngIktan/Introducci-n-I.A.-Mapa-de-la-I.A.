# Daniel Alejandro Flores Sepulveda
# Programa para realizar la Búsqueda de Haz Local en un problema de optimización combinatoria.

import random

# Función de evaluación (a minimizar)
def funcion_evaluacion(solucion):
    return sum(solucion)  # Ejemplo de una función que suma los elementos de la solución

# Generar una solución aleatoria
def generar_solucion(n):
    return [random.randint(0, 1) for _ in range(n)]  # Ejemplo de solución binaria aleatoria

# Generar vecinos de una solución
def generar_vecinos(solucion):
    vecinos = []
    for i in range(len(solucion)):
        vecino = solucion.copy()
        vecino[i] = 1 - vecino[i]  # Cambiar un bit
        vecinos.append(vecino)
    return vecinos

# Algoritmo de Búsqueda de Haz Local
def busqueda_haz_local(n, tamano_haz, iteraciones_maximas):
    # Generar soluciones iniciales
    haz = [generar_solucion(n) for _ in range(tamano_haz)]
    
    # Iterar hasta alcanzar el límite de iteraciones
    for iteracion in range(iteraciones_maximas):
        # Generar vecinos de todas las soluciones del haz
        vecinos_haz = [generar_vecinos(solucion) for solucion in haz]
        
        # Aplanar la lista de vecinos
        vecinos = [vecino for sublist in vecinos_haz for vecino in sublist]
        
        # Seleccionar los mejores vecinos
        vecinos.sort(key=funcion_evaluacion)
        haz = vecinos[:tamano_haz]
    
    # Seleccionar la mejor solución del haz
    mejor_solucion = min(haz, key=funcion_evaluacion)
    mejor_valor = funcion_evaluacion(mejor_solucion)
    
    return mejor_solucion, mejor_valor

# Parámetros del problema
n = 10  # Tamaño de la solución
tamano_haz = 5  # Tamaño del haz
iteraciones_maximas = 100  # Número máximo de iteraciones

# Ejecutar el algoritmo de Búsqueda de Haz Local
mejor_solucion, mejor_valor = busqueda_haz_local(n, tamano_haz, iteraciones_maximas)

# Mostrar resultados
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
