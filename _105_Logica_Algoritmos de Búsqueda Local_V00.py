# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de algoritmos de búsqueda local (Ascenso de Colinas y Enfriamiento Simulado).

import random
import math

# Función de evaluación que queremos maximizar
def evaluacion(solucion):
    # Por ejemplo, podría ser una función que calcule el valor de una solución
    return sum(solucion)

# Algoritmo de ascenso de colinas
def hill_climbing(n_iter):
    solucion_actual = [random.randint(0, 1) for _ in range(10)]  # Solución inicial aleatoria
    valor_actual = evaluacion(solucion_actual)

    for _ in range(n_iter):
        vecino = solucion_actual[:]  # Copia de la solución actual
        idx = random.randint(0, len(solucion_actual) - 1)  # Seleccionar una posición aleatoria
        vecino[idx] = 1 if vecino[idx] == 0 else 0  # Cambiar el valor de la posición seleccionada

        valor_vecino = evaluacion(vecino)
        if valor_vecino > valor_actual:
            solucion_actual = vecino
            valor_actual = valor_vecino

    return solucion_actual, valor_actual

# Algoritmo de enfriamiento simulado
def simulated_annealing(T, n_iter, alpha):
    solucion_actual = [random.randint(0, 1) for _ in range(10)]  # Solución inicial aleatoria
    valor_actual = evaluacion(solucion_actual)

    for i in range(n_iter):
        temperatura = T / (i + 1)
        vecino = solucion_actual[:]  # Copia de la solución actual
        idx = random.randint(0, len(solucion_actual) - 1)  # Seleccionar una posición aleatoria
        vecino[idx] = 1 if vecino[idx] == 0 else 0  # Cambiar el valor de la posición seleccionada

        valor_vecino = evaluacion(vecino)
        delta_valor = valor_vecino - valor_actual

        if delta_valor > 0 or random.random() < math.exp(delta_valor / temperatura):
            solucion_actual = vecino
            valor_actual = valor_vecino

    return solucion_actual, valor_actual

# Ejemplo de uso del algoritmo de ascenso de colinas
if __name__ == "__main__":
    solucion_hc, valor_hc = hill_climbing(1000)
    print("Solución encontrada con Ascenso de Colinas:", solucion_hc)
    print("Valor de la solución:", valor_hc)

# Ejemplo de uso del algoritmo de enfriamiento simulado
if __name__ == "__main__":
    solucion_sa, valor_sa = simulated_annealing(100, 1000, 0.95)
    print("Solución encontrada con Enfriamiento Simulado:", solucion_sa)
    print("Valor de la solución:", valor_sa)
