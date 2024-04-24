# Autor: Daniel Alejandro Flores Sepulveda
# Implementación del algoritmo de agrupamiento k-medias

import numpy as np

class KMeans:
    def __init__(self, n_clusters, max_iter=100, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        n_samples, n_features = X.shape

        # Inicialización de centroides
        self.centroids = X[np.random.choice(n_samples, self.n_clusters, replace=False)]

        # Algoritmo k-medias
        for _ in range(self.max_iter):
            # Asignar puntos al cluster más cercano
            labels = self._assign_clusters(X)

            # Actualizar centroides
            new_centroids = self._update_centroids(X, labels)

            # Comprobar convergencia
            if np.allclose(self.centroids, new_centroids, atol=self.tol):
                break

            self.centroids = new_centroids

    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis, :] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])
        return new_centroids

# Datos de ejemplo
np.random.seed(0)
X = np.concatenate([np.random.normal(loc=0, scale=1, size=(100, 2)),
                    np.random.normal(loc=5, scale=1, size=(100, 2))])

# Agrupamiento k-medias
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Obtener etiquetas de los clústeres
labels = kmeans._assign_clusters(X)

# Imprimir centroides y etiquetas de los clústeres
print("Centroides:")
print(kmeans.centroids)
print("Etiquetas de los clústeres:")
print(labels)
