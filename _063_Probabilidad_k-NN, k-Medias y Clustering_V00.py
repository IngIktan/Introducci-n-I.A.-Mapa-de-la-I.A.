# Autor: Daniel Alejandro Flores Sepulveda
# Programa para implementar k-NN, k-Medias y Clustering

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Algoritmo k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predecir el resultado
x_new = [0, 2]
prediction = knn.predict([x_new])

print("Predicción con k-NN:", prediction)

# Algoritmo k-Medias
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Visualizar los resultados del clustering
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
plt.title("Clustering con k-Medias")
plt.show()
