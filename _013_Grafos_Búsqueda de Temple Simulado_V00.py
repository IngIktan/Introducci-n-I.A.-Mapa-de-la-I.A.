# Daniel Alejandro Flores Sepulveda
# Programa para realizar la Búsqueda de Temple Simulado en un problema de optimización combinatoria.

import math
import random

# Función de evaluación (a minimizar)
def funcion_evaluacion(solucion):
    return sum(solucion)  # Ejemplo de una función que suma los elementos de la solución

# Generar una solución inicial aleatoria
def generar_solucion_inicial(n):
    return [random.randint(0, 1) for _ in range(n)]  # Ejemplo de solución binaria aleatoria

# Generar un vecino de una solución
def generar_vecino(solucion):
    vecino = solucion.copy()
    indice = random.randint(0, len(solucion) - 1)
    vecino[indice] = 1 - vecino[indice]  # Cambiar un bit aleatorio
    return vecino

# Función de probabilidad para aceptar movimientos peores
def probabilidad_aceptacion(delta, temperatura):
    if delta < 0:
        return 1.0  # Si el movimiento mejora la solución, aceptarlo siempre
    return math.exp(-delta / temperatura)  # Si el movimiento empeora la solución, calcular la probabilidad de aceptarlo

# Algoritmo de Temple Simulado
def temple_simulado(n, iteraciones_maximas, temperatura_inicial, enfriamiento):
    # Generar solución inicial
    solucion_actual = generar_solucion_inicial(n)
    mejor_solucion = solucion_actual.copy()
    mejor_valor = funcion_evaluacion(mejor_solucion)
    
    # Inicializar temperatura
    temperatura = temperatura_inicial
    
    # Iterar hasta alcanzar el límite de iteraciones
    for iteracion in range(iteraciones_maximas):
        # Generar un vecino aleatorio
        vecino = generar_vecino(solucion_actual)
        
        # Evaluar el cambio en la función objetivo
        delta = funcion_evaluacion(vecino) - funcion_evaluacion(solucion_actual)
        
        # Decidir si se acepta el movimiento
        if random.random() < probabilidad_aceptacion(delta, temperatura):
            solucion_actual = vecino
        
        # Actualizar mejor solución encontrada
        if funcion_evaluacion(solucion_actual) < funcion_evaluacion(mejor_solucion):
            mejor_solucion = solucion_actual.copy()
            mejor_valor = funcion_evaluacion(mejor_solucion)
        
        # Enfriar la temperatura
        temperatura *= enfriamiento
    
    return mejor_solucion, mejor_valor

# Parámetros del problema
n = 10  # Tamaño de la solución
iteraciones_maximas = 1000  # Número máximo de iteraciones
temperatura_inicial = 100.0  # Temperatura inicial
enfriamiento = 0.99  # Factor de enfriamiento

# Ejecutar el algoritmo de Temple Simulado
mejor_solucion, mejor_valor = temple_simulado(n, iteraciones_maximas, temperatura_inicial, enfriamiento)

# Mostrar resultados
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
