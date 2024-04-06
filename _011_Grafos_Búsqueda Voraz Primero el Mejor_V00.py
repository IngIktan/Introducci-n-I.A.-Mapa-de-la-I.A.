# Daniel Alejandro Flores Sepulveda
# Programa para realizar la búsqueda de Ascensión de Colinas en un problema de optimización.

import random

# Función de evaluación (a minimizar)
def funcion_evaluacion(x):
    return x**2  # Ejemplo de una función cuadrática que queremos minimizar

# Función de Ascensión de Colinas
def ascension_colinas():
    # Estado inicial aleatorio
    estado_actual = random.uniform(-10, 10)
    mejor_solucion = estado_actual
    mejor_valor = funcion_evaluacion(mejor_solucion)
    
    # Iteraciones máximas
    iteraciones_maximas = 100
    iteracion = 0
    
    while iteracion < iteraciones_maximas:
        # Generar un vecino aleatorio
        vecino = estado_actual + random.uniform(-0.5, 0.5)
        
        # Evaluar la función en el vecino
        valor_vecino = funcion_evaluacion(vecino)
        
        # Si el vecino mejora la solución actual, actualizar
        if valor_vecino < mejor_valor:
            mejor_solucion = vecino
            mejor_valor = valor_vecino
        
        # Actualizar el estado actual para la siguiente iteración
        estado_actual = vecino
        iteracion += 1
    
    return mejor_solucion, mejor_valor

# Ejecutar la búsqueda de Ascensión de Colinas
mejor_solucion, mejor_valor = ascension_colinas()

# Mostrar resultados
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
