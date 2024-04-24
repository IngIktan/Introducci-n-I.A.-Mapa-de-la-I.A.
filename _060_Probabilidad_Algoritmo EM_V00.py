# Autor: Daniel Alejandro Flores Sepulveda
# Implementación del algoritmo Expectation-Maximization (EM) para un modelo de mezcla de Gaussianas

import numpy as np
from scipy.stats import multivariate_normal

class GaussianMixtureModel:
    def __init__(self, n_components, max_iter=100, tol=1e-4):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        n_samples, n_features = X.shape

        # Inicialización de parámetros
        self.weights = np.ones(self.n_components) / self.n_components
        self.means = X[np.random.choice(n_samples, self.n_components, replace=False)]
        self.covariances = np.array([np.cov(X.T) for _ in range(self.n_components)])

        # Algoritmo EM
        for _ in range(self.max_iter):
            # Paso E (Expectation)
            responsibilities = self._compute_responsibilities(X)

            # Paso M (Maximization)
            self._update_parameters(X, responsibilities)

            # Calcular log-verosimilitud
            log_likelihood = self._compute_log_likelihood(X)
            if len(log_likelihood) > 1 and np.abs(log_likelihood[-1] - log_likelihood[-2]) < self.tol:
                break

    def _compute_responsibilities(self, X):
        responsibilities = np.zeros((X.shape[0], self.n_components))
        for k in range(self.n_components):
            responsibilities[:, k] = self.weights[k] * multivariate_normal.pdf(X, self.means[k], self.covariances[k])
        responsibilities /= np.sum(responsibilities, axis=1, keepdims=True)
        return responsibilities

    def _update_parameters(self, X, responsibilities):
        Nk = np.sum(responsibilities, axis=0)
        self.weights = Nk / X.shape[0]
        self.means = np.dot(responsibilities.T, X) / Nk[:, np.newaxis]
        for k in range(self.n_components):
            diff = X - self.means[k]
            self.covariances[k] = np.dot(responsibilities[:, k] * diff.T, diff) / Nk[k]

    def _compute_log_likelihood(self, X):
        log_likelihood = []
        for k in range(self.n_components):
            likelihood = self.weights[k] * multivariate_normal.pdf(X, self.means[k], self.covariances[k])
            log_likelihood.append(np.sum(np.log(likelihood)))
        return log_likelihood

# Datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.normal(loc=0, scale=1, size=(100, 2)),
                    np.random.normal(loc=5, scale=1, size=(100, 2))])

# Entrenamiento del modelo de mezcla de Gaussianas
model = GaussianMixtureModel(n_components=2)
model.fit(X)

# Parámetros aprendidos
print("Pesos:", model.weights)
print("Medias:", model.means)
print("Covarianzas:", model.covariances)
