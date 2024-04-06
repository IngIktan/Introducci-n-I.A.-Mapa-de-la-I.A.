# Daniel Alejandro Flores Sepulveda
# Programa para realizar un Algoritmo Genético en un problema de optimización combinatoria.

import random

# Función de evaluación (a minimizar)
def funcion_evaluacion(solucion):
    return sum(solucion)  # Ejemplo de una función que suma los elementos de la solución

# Generar una solución aleatoria
def generar_solucion(n):
    return [random.randint(0, 1) for _ in range(n)]  # Ejemplo de solución binaria aleatoria

# Operador de selección (torneo)
def seleccion_torneo(poblacion, k):
    seleccionados = []
    for _ in range(k):
        muestra = random.sample(poblacion, 2)  # Seleccionar dos individuos aleatorios
        seleccionados.append(min(muestra, key=funcion_evaluacion))  # Seleccionar el mejor de la muestra
    return seleccionados

# Operador de cruce (punto único)
def cruce_punto_unico(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)  # Seleccionar un punto de cruce aleatorio
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Operador de mutación (bit flip)
def mutacion_bit_flip(solucion, probabilidad):
    for i in range(len(solucion)):
        if random.random() < probabilidad:
            solucion[i] = 1 - solucion[i]  # Cambiar el bit con cierta probabilidad
    return solucion

# Algoritmo Genético
def algoritmo_genetico(n, tamano_poblacion, probabilidad_mutacion, iteraciones_maximas):
    # Generar población inicial aleatoria
    poblacion = [generar_solucion(n) for _ in range(tamano_poblacion)]
    
    # Iterar hasta alcanzar el límite de iteraciones
    for iteracion in range(iteraciones_maximas):
        # Seleccionar padres mediante torneo
        padres = seleccion_torneo(poblacion, 2)
        
        # Aplicar operador de cruce (punto único)
        hijos = cruce_punto_unico(padres[0], padres[1])
        
        # Aplicar operador de mutación (bit flip)
        hijos_mutados = [mutacion_bit_flip(hijo, probabilidad_mutacion) for hijo in hijos]
        
        # Reemplazar peores soluciones de la población por los hijos mutados
        poblacion.extend(hijos_mutados)
        poblacion = sorted(poblacion, key=funcion_evaluacion)[:tamano_poblacion]  # Seleccionar las mejores soluciones
    
    # Seleccionar la mejor solución de la población final
    mejor_solucion = min(poblacion, key=funcion_evaluacion)
    mejor_valor = funcion_evaluacion(mejor_solucion)
    
    return mejor_solucion, mejor_valor

# Parámetros del problema
n = 10  # Tamaño de la solución
tamano_poblacion = 50  # Tamaño de la población
probabilidad_mutacion = 0.1  # Probabilidad de mutación
iteraciones_maximas = 100  # Número máximo de iteraciones

# Ejecutar el algoritmo Genético
mejor_solucion, mejor_valor = algoritmo_genetico(n, tamano_poblacion, probabilidad_mutacion, iteraciones_maximas)

# Mostrar resultados
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
