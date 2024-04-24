# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa una Red de Hopfield en Python.

import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        # Calcular los pesos sinápticos utilizando la regla de Hebb
        for pattern in patterns:
            pattern = np.array(pattern)
            self.weights += np.outer(pattern, pattern)
            np.fill_diagonal(self.weights, 0)

    def predict(self, pattern, max_iterations=100):
        pattern = np.array(pattern)
        for _ in range(max_iterations):
            new_pattern = np.sign(np.dot(self.weights, pattern))
            if np.array_equal(new_pattern, pattern):
                return new_pattern
            pattern = new_pattern
        return pattern

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de la red de Hopfield con 4 neuronas
    hopfield_net = HopfieldNetwork(4)

    # Definimos patrones para entrenar la red
    patterns = [[1, 1, 1, -1], [-1, -1, 1, 1], [-1, 1, -1, -1]]

    # Entrenamos la red con los patrones
    hopfield_net.train(patterns)

    # Probamos la red con un patrón incompleto
    test_pattern = [1, -1, 1, -1]
    predicted_pattern = hopfield_net.predict(test_pattern)
    print("Patrón original:", test_pattern)
    print("Patrón recuperado:", predicted_pattern)
