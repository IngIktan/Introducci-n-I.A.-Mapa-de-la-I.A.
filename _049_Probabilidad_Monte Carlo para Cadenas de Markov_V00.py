# Autor: Daniel Alejandro Flores Sepulveda
# Programa para realizar Monte Carlo para Cadenas de Markov (MCMC) con el método de Metropolis-Hastings
import numpy as np

# Función objetivo (distribución de probabilidad deseada)
def target_distribution(x):
    return np.exp(-x ** 2)  # Distribución exponencial

# Propuesta de transición (distribución de probabilidad para generar nuevos estados)
def transition_proposal(x):
    return np.random.normal(x, 1)  # Distribución normal con media x y desviación estándar 1

# Algoritmo de Monte Carlo para Cadenas de Markov (MCMC) con Metropolis-Hastings
def metropolis_hastings(target_distribution, transition_proposal, initial_state, n_samples):
    samples = [initial_state]  # Inicializar la secuencia de muestras con el estado inicial
    current_state = initial_state  # Inicializar el estado actual con el estado inicial
    for _ in range(n_samples):
        proposed_state = transition_proposal(current_state)  # Generar un estado propuesto
        acceptance_ratio = min(1, target_distribution(proposed_state) / target_distribution(current_state))
        if np.random.rand() < acceptance_ratio:  # Aceptar o rechazar el estado propuesto
            current_state = proposed_state
        samples.append(current_state)  # Agregar el estado actual a la secuencia de muestras
    return samples

# Parámetros del algoritmo
initial_state = 0  # Estado inicial
n_samples = 10000  # Número de muestras a generar

# Generar muestras utilizando el algoritmo de Metropolis-Hastings
samples = metropolis_hastings(target_distribution, transition_proposal, initial_state, n_samples)

# Mostrar resultados con solo tres dígitos
print("Muestras generadas mediante MCMC con Metropolis-Hastings:")
print([round(sample, 3) for sample in samples])
