# Autor: Daniel Alejandro Flores Sepulveda 
# Programa para implementar funciones de activación en una red neuronal

import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de activación y sus derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.square(tanh(x))

# Valores de entrada
x = np.linspace(-5, 5, 100)

# Calcular las salidas de cada función de activación y sus derivadas
y_sigmoid = sigmoid(x)
y_sigmoid_deriv = sigmoid_derivative(x)

y_relu = relu(x)
y_relu_deriv = relu_derivative(x)

y_tanh = tanh(x)
y_tanh_deriv = tanh_derivative(x)

# Graficar las funciones de activación y sus derivadas
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_sigmoid, label='Sigmoid')
plt.title('Sigmoid')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, y_sigmoid_deriv, label='Sigmoid Derivative')
plt.title('Sigmoid Derivative')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, y_relu, label='ReLU')
plt.title('ReLU')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, y_relu_deriv, label='ReLU Derivative')
plt.title('ReLU Derivative')
plt.legend()

plt.tight_layout()
plt.show()
