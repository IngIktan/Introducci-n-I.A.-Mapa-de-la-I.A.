# Autor: Daniel Alejandro Flores Sepulveda
# Implementación de un Modelo de Markov Oculto (HMM) utilizando la biblioteca hmmlearn

from hmmlearn import hmm
import numpy as np

# Datos de entrada
X = np.array([[0], [1], [0], [1], [0], [0]])

# Crear y ajustar el modelo HMM
model = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
model.fit(X)

# Generar secuencia de estados ocultos
hidden_states = model.predict(X)

# Imprimir secuencia de estados ocultos
print("Secuencia de estados ocultos:")
print(hidden_states)
