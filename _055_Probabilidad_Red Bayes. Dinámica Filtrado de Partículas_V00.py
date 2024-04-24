# Autor: Daniel Alejandro Flores Sepulveda
# Programa de Filtrado de particulas 

import numpy as np

class ParticleFilter:
    def __init__(self, transition_model, observation_model, n_particles):
        self.transition_model = transition_model  # Modelo de transición de estado
        self.observation_model = observation_model  # Modelo de observación
        self.n_particles = n_particles  # Número de partículas

    def update(self, observations):
        # Inicializar partículas
        particles = np.random.rand(self.n_particles)

        # Actualizar partículas
        for observation in observations:
            # Muestrear nuevas partículas utilizando el modelo de transición
            particles = self.transition_model(particles)

            # Ponderar partículas basado en las observaciones
            weights = self.observation_model(observation, particles)
            weights /= np.sum(weights)  # Normalizar los pesos

            # Resampling (remuestreo) basado en los pesos
            indices = np.random.choice(np.arange(self.n_particles), size=self.n_particles, p=weights)
            particles = particles[indices]

        return particles

# Función de transición de estado (ejemplo: caminata aleatoria)
def transition_model(particles):
    return particles + np.random.normal(0, 1, len(particles))

# Función de observación (ejemplo: distribución normal)
def observation_model(observation, particles):
    return np.exp(-0.5 * (particles - observation) ** 2)

# Parámetros del filtrado de partículas
n_particles = 1000  # Número de partículas
n_observations = 10  # Número de observaciones

# Crear instancia del filtro de partículas
particle_filter = ParticleFilter(transition_model, observation_model, n_particles)

# Observaciones simuladas
observations = np.random.normal(0, 1, n_observations)

# Filtrado de partículas
filtered_particles = particle_filter.update(observations)

print("Partículas filtradas:")
print(filtered_particles)
