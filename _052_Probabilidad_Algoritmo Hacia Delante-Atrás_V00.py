# Autor: Daniel Alejandro Flores Sepulveda
# Programa para implementar el algoritmo Hacia Delante-Atrás en un Modelo Oculto de Markov

import numpy as np

# Función para calcular la probabilidad hacia adelante
def forward_algorithm(observations, initial_distribution, transition_matrix, emission_matrix):
    n_states = transition_matrix.shape[0]
    n_observations = len(observations)
    forward_probabilities = np.zeros((n_observations, n_states))

    # Paso inicial: calcular la probabilidad hacia adelante para el primer paso de tiempo
    forward_probabilities[0] = initial_distribution * emission_matrix[observations[0]]

    # Paso hacia adelante: calcular la probabilidad hacia adelante para los pasos de tiempo restantes
    for t in range(1, n_observations):
        for j in range(n_states):
            forward_probabilities[t, j] = np.sum(forward_probabilities[t - 1] * transition_matrix[:, j]) * emission_matrix[observations[t], j]

    return forward_probabilities

# Función para calcular la probabilidad hacia atrás
def backward_algorithm(observations, transition_matrix, emission_matrix):
    n_states = transition_matrix.shape[0]
    n_observations = len(observations)
    backward_probabilities = np.zeros((n_observations, n_states))

    # Paso final: asignar 1 a todas las probabilidades hacia atrás para el último paso de tiempo
    backward_probabilities[-1] = 1

    # Paso hacia atrás: calcular la probabilidad hacia atrás para los pasos de tiempo anteriores
    for t in range(n_observations - 2, -1, -1):
        for i in range(n_states):
            backward_probabilities[t, i] = np.sum(transition_matrix[i] * emission_matrix[observations[t + 1]] * backward_probabilities[t + 1])

    return backward_probabilities

# Datos de ejemplo
observations = [0, 1, 0]  # Datos observados
initial_distribution = np.array([0.5, 0.5])  # Distribución inicial de estados
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
emission_matrix = np.array([[0.9, 0.1], [0.2, 0.8]])  # Matriz de emisión

# Calcular la probabilidad hacia adelante y hacia atrás
forward_probabilities = forward_algorithm(observations, initial_distribution, transition_matrix, emission_matrix)
backward_probabilities = backward_algorithm(observations, transition_matrix, emission_matrix)

# Imprimir resultados
print("Probabilidades hacia adelante:")
print(forward_probabilities)
print("\nProbabilidades hacia atrás:")
print(backward_probabilities)
