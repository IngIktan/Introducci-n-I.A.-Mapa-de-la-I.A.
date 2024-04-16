# Daniel Alejandro Flores Sepulveda
# Programa para simular un modelo de Markov simple

import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states

    def next_state(self, current_state):
        next_state_index = np.random.choice(len(self.states), p=self.transition_matrix[current_state])
        return next_state_index  # Devolvemos el índice en lugar del estado

# Definir la matriz de transición y los estados
transition_matrix = [[0.7, 0.3],   # Probabilidades de pasar de A a A y A a B
                     [0.4, 0.6]]   # Probabilidades de pasar de B a A y B a B
states = ['A', 'B']

# Crear el objeto MarkovChain
markov_chain = MarkovChain(transition_matrix, states)

# Estado inicial
current_state = 0  # A es el estado inicial

# Simular transiciones de estado
print("Secuencia de estados generada por el modelo de Markov:")
for _ in range(10):
    print(states[current_state])
    current_state = markov_chain.next_state(current_state)
