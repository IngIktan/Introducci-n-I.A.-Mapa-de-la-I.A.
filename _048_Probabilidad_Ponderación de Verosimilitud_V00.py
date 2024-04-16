# Autor: Daniel Alejandro Flores Sepulveda
# Programa para realizar ponderación de verosimilitud en un modelo de regresión lineal

import numpy as np

# Datos observados
X = np.array([1, 2, 3, 4, 5])  # Variables independientes
y = np.array([3, 5, 7, 9, 11])  # Variable dependiente

# Parámetros del modelo
beta_0 = 0  # Intercepto
beta_1 = 0  # Pendiente

# Hiperparámetros de la distribución a priori de los parámetros
mu_0 = 0  # Media del prior para beta_0
sigma_0 = 1  # Desviación estándar del prior para beta_0
mu_1 = 0  # Media del prior para beta_1
sigma_1 = 1  # Desviación estándar del prior para beta_1

# Ponderación de verosimilitud
def likelihood_weighting(X, y, beta_0, beta_1, mu_0, sigma_0, mu_1, sigma_1):
    n = len(X)
    likelihoods = []
    for i in range(n):
        x_i = X[i]
        y_i = y[i]
        # Calcula la verosimilitud para la i-ésima observación
        likelihood_beta_0 = (1 / np.sqrt(2 * np.pi * sigma_0 ** 2)) * np.exp(-0.5 * ((beta_0 - mu_0) / sigma_0) ** 2)
        likelihood_beta_1 = (1 / np.sqrt(2 * np.pi * sigma_1 ** 2)) * np.exp(-0.5 * ((beta_1 - mu_1) / sigma_1) ** 2)
        # Pondera la verosimilitud por la probabilidad a priori de los parámetros
        weighted_likelihood = likelihood_beta_0 * likelihood_beta_1
        likelihoods.append(weighted_likelihood)
    # Normaliza las ponderaciones
    total_likelihood = sum(likelihoods)
    normalized_likelihoods = [likelihood / total_likelihood for likelihood in likelihoods]
    return normalized_likelihoods

# Realiza la ponderación de verosimilitud
weights = likelihood_weighting(X, y, beta_0, beta_1, mu_0, sigma_0, mu_1, sigma_1)

# Muestra los pesos resultantes
print("Pesos de verosimilitud ponderados:", weights)
# Autor: Daniel Alejandro Flores Sepulveda
# Programa para realizar ponderación de verosimilitud en un modelo de regresión lineal

import numpy as np

# Datos observados
X = np.array([1, 2, 3, 4, 5])  # Variables independientes
y = np.array([3, 5, 7, 9, 11])  # Variable dependiente

# Parámetros del modelo
beta_0 = 0  # Intercepto
beta_1 = 0  # Pendiente

# Hiperparámetros de la distribución a priori de los parámetros
mu_0 = 0  # Media del prior para beta_0
sigma_0 = 1  # Desviación estándar del prior para beta_0
mu_1 = 0  # Media del prior para beta_1
sigma_1 = 1  # Desviación estándar del prior para beta_1

# Ponderación de verosimilitud
def likelihood_weighting(X, y, beta_0, beta_1, mu_0, sigma_0, mu_1, sigma_1):
    n = len(X)
    likelihoods = []
    for i in range(n):
        x_i = X[i]
        y_i = y[i]
        # Calcula la verosimilitud para la i-ésima observación
        likelihood_beta_0 = (1 / np.sqrt(2 * np.pi * sigma_0 ** 2)) * np.exp(-0.5 * ((beta_0 - mu_0) / sigma_0) ** 2)
        likelihood_beta_1 = (1 / np.sqrt(2 * np.pi * sigma_1 ** 2)) * np.exp(-0.5 * ((beta_1 - mu_1) / sigma_1) ** 2)
        # Pondera la verosimilitud por la probabilidad a priori de los parámetros
        weighted_likelihood = likelihood_beta_0 * likelihood_beta_1
        likelihoods.append(weighted_likelihood)
    # Normaliza las ponderaciones
    total_likelihood = sum(likelihoods)
    normalized_likelihoods = [likelihood / total_likelihood for likelihood in likelihoods]
    return normalized_likelihoods

# Realiza la ponderación de verosimilitud
weights = likelihood_weighting(X, y, beta_0, beta_1, mu_0, sigma_0, mu_1, sigma_1)

# Muestra los pesos resultantes
print("Pesos de verosimilitud ponderados:", weights)
