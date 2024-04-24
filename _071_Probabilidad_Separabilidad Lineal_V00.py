# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa un Perceptrón para clasificación binaria.

import numpy as np

class Perceptron:
    def __init__(self, num_features):
        self.weights = np.random.rand(num_features)  # Inicializamos los pesos de forma aleatoria
        self.bias = np.random.rand()  # Inicializamos el sesgo de forma aleatoria

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias  # Calculamos la suma ponderada de las entradas
        return 1 if summation > 0 else 0  # Aplicamos la función de activación escalón

# Función para generar datos linealmente separables
def generate_linearly_separable_data(num_samples, num_features):
    X = np.random.rand(num_samples, num_features)  # Generamos muestras aleatorias
    true_weights = np.random.rand(num_features)  # Generamos pesos verdaderos aleatorios para el hiperplano
    true_bias = np.random.rand()  # Generamos sesgo verdadero aleatorio para el hiperplano
    y = np.dot(X, true_weights) + true_bias > 0  # Aplicamos la función de decisión
    y = y.astype(int)  # Convertimos a valores enteros (0 o 1)
    return X, y

# Generamos datos linealmente separables para probar el Perceptrón
num_samples = 100
num_features = 2
X, y = generate_linearly_separable_data(num_samples, num_features)

# Creamos y entrenamos el Perceptrón
perceptron = Perceptron(num_features)
for _ in range(100):  # Iteramos para entrenar el perceptrón (puede ser necesario ajustar este valor)
    for i in range(num_samples):
        prediction = perceptron.predict(X[i])
        perceptron.weights += 0.1 * (y[i] - prediction) * X[i]  # Actualizamos los pesos
        perceptron.bias += 0.1 * (y[i] - prediction)  # Actualizamos el sesgo

# Evaluamos el Perceptrón
correct = 0
for i in range(num_samples):
    prediction = perceptron.predict(X[i])
    if prediction == y[i]:
        correct += 1

accuracy = correct / num_samples
print("Accuracy:", accuracy)
