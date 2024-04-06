# Daniel Alejandro Flores Sepulveda
# Programa para realizar la Búsqueda Tabú en un problema de optimización combinatoria.

import random

# Función de evaluación (a minimizar)
def funcion_evaluacion(solucion):
    return sum(solucion)  # Ejemplo de una función que suma los elementos de la solución

# Generar una solución inicial aleatoria
def generar_solucion_inicial(n):
    return [random.randint(0, 1) for _ in range(n)]  # Ejemplo de solución binaria aleatoria

# Generar vecinos de una solución
def generar_vecinos(solucion):
    vecinos = []
    for i in range(len(solucion)):
        vecino = solucion.copy()
        vecino[i] = 1 - vecino[i]  # Cambiar un bit
        vecinos.append(vecino)
    return vecinos

# Algoritmo de Búsqueda Tabú
def busqueda_tabu(n, iteraciones_maximas):
    # Generar solución inicial
    solucion_actual = generar_solucion_inicial(n)
    mejor_solucion = solucion_actual.copy()
    mejor_valor = funcion_evaluacion(mejor_solucion)
    
    # Inicializar lista tabú
    lista_tabu = []
    
    # Iterar hasta alcanzar el límite de iteraciones
    for iteracion in range(iteraciones_maximas):
        # Generar vecinos
        vecinos = generar_vecinos(solucion_actual)
        
        # Evaluar vecinos y encontrar el mejor no tabú
        mejor_vecino = None
        mejor_valor_vecino = float('inf')
        for vecino in vecinos:
            if vecino not in lista_tabu:
                valor_vecino = funcion_evaluacion(vecino)
                if valor_vecino < mejor_valor_vecino:
                    mejor_vecino = vecino
                    mejor_valor_vecino = valor_vecino
        
        # Actualizar solución actual y lista tabú
        solucion_actual = mejor_vecino
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > 5:  # Longitud máxima de la lista tabú
            lista_tabu.pop(0)  # Eliminar el primer elemento
        
        # Actualizar mejor solución encontrada
        if mejor_valor_vecino < mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = mejor_valor_vecino
    
    return mejor_solucion, mejor_valor

# Parámetros del problema
n = 10  # Tamaño de la solución
iteraciones_maximas = 100  # Número máximo de iteraciones

# Ejecutar el algoritmo de Búsqueda Tabú
mejor_solucion, mejor_valor = busqueda_tabu(n, iteraciones_maximas)

# Mostrar resultados
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
