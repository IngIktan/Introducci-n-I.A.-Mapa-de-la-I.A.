# Autor: Daniel Alejandro Flores Sepulveda
# Programa para simular un proceso de Markov de primer orden

import numpy as np

# Definición de la matriz de transición
transition_matrix = np.array([[0.8, 0.2],  # Probabilidades de transición del estado 0
                              [0.3, 0.7]]) # Probabilidades de transición del estado 1

# Función para simular el proceso de Markov
def markov_process(initial_state, n_steps):
    states = [initial_state]  # Lista para almacenar los estados generados
    current_state = initial_state  # Inicializar el estado actual con el estado inicial
    for _ in range(n_steps):
        # Generar el siguiente estado según la matriz de transición
        next_state = np.random.choice([0, 1], p=transition_matrix[current_state])
        states.append(next_state)  # Agregar el siguiente estado a la lista de estados
        current_state = next_state  # Actualizar el estado actual
    return states

# Parámetros del proceso de Markov
initial_state = 0  # Estado inicial
n_steps = 100  # Número de pasos en el proceso

# Simular el proceso de Markov
states = markov_process(initial_state, n_steps)

# Mostrar resultados
print("Secuencia de estados generada por el proceso de Markov:")
print(states)
