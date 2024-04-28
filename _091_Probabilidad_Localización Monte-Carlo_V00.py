# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de localización de Monte Carlo (filtro de partículas) en Python.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
n_particles = 1000  # Número de partículas
n_landmarks = 5  # Número de puntos de referencia (landmarks)
measurement_noise = 0.1  # Ruido de las mediciones
movement_noise = 0.1  # Ruido del movimiento

# Generar puntos de referencia aleatorios en el plano XY
landmarks = np.random.uniform(-5, 5, size=(n_landmarks, 2))

# Función para simular mediciones de rango a los puntos de referencia
def sense(x, landmarks):
    distances = np.linalg.norm(landmarks - x[:2], axis=1)
    return distances + np.random.normal(0, measurement_noise, size=distances.shape)

# Función para simular el movimiento del robot
def move(x, u):
    return x + u + np.random.normal(0, movement_noise, size=x.shape)

# Inicializar las partículas con una distribución uniforme en el espacio
particles = np.random.uniform(-5, 5, size=(n_particles, 3))

# Iterar sobre el tiempo
for t in range(1, 101):
    # Simular el movimiento del robot
    movement = np.array([0.1, 0.1, 0.01])  # Movimiento lineal y angular
    particles = np.array([move(particle, movement) for particle in particles])

    # Simular mediciones de rango
    measurements = np.array([sense(particle, landmarks) for particle in particles])

    # Calcular los pesos de las partículas
    weights = np.exp(-0.5 * np.sum((measurements - np.linalg.norm(landmarks, axis=1))**2 / measurement_noise**2, axis=1))

    # Normalizar los pesos
    weights /= np.sum(weights)

    # Resampling
    indices = np.random.choice(range(n_particles), size=n_particles, p=weights)
    particles = particles[indices]

    # Visualizar las partículas y los puntos de referencia
    plt.figure(figsize=(8, 6))
    plt.title('Localización de Monte Carlo - Iteración {}'.format(t))
    plt.scatter(particles[:, 0], particles[:, 1], s=5, c='b', label='Partículas')
    plt.scatter(landmarks[:, 0], landmarks[:, 1], c='r', marker='x', label='Landmarks')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.xlabel('Posición en X')
    plt.ylabel('Posición en Y')
    plt.legend()
    plt.grid(True)
    plt.show()
