# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa la retropropagación del error en Python utilizando NumPy.

import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inicializamos los pesos de manera aleatoria
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        
        # Inicializamos los sesgos de manera aleatoria
        self.bias_hidden = np.random.rand(self.hidden_size)
        self.bias_output = np.random.rand(self.output_size)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def feedforward(self, inputs):
        # Calculamos las salidas de la capa oculta
        hidden_inputs = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_outputs = self.sigmoid(hidden_inputs)
        
        # Calculamos las salidas finales
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_output) + self.bias_output
        final_outputs = self.sigmoid(final_inputs)
        
        return final_outputs
    
    def train(self, inputs, targets, learning_rate):
        # Feedforward
        hidden_inputs = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_outputs = self.sigmoid(hidden_inputs)
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_output) + self.bias_output
        final_outputs = self.sigmoid(final_inputs)
        
        # Retropropagación del error
        output_errors = targets - final_outputs
        output_delta = output_errors * self.sigmoid_derivative(final_outputs)
        
        hidden_errors = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_errors * self.sigmoid_derivative(hidden_outputs)
        
        # Actualizamos los pesos y sesgos
        self.weights_hidden_output += np.dot(hidden_outputs.T, output_delta) * learning_rate
        self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de la red neuronal
    nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
    
    # Definimos un conjunto de datos de entrenamiento
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])
    
    # Entrenamos la red neuronal
    for i in range(10000):
        nn.train(inputs, targets, learning_rate=0.1)
    
    # Probamos la red neuronal con nuevos datos
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for input in test_inputs:
        print("Input:", input, "Output:", nn.feedforward(input))
