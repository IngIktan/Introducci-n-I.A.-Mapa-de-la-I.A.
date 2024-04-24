import numpy as np

class HiddenMarkovModel:
    def __init__(self, transition_probs, emission_probs, initial_probs):
        self.transition_probs = transition_probs
        self.emission_probs = emission_probs
        self.initial_probs = initial_probs
        self.num_states = len(transition_probs)
        self.num_observation_symbols = len(emission_probs[0])

    def generate_sequence(self, length):
        # Generar una secuencia de observaciones
        observations = []
        # Escoger el estado inicial
        current_state = np.random.choice(self.num_states, p=self.initial_probs)
        for _ in range(length):
            # Generar una observación basada en el estado actual
            observation = np.random.choice(self.num_observation_symbols, p=self.emission_probs[current_state])
            observations.append(observation)
            # Transicionar al siguiente estado basado en la matriz de transición
            current_state = np.random.choice(self.num_states, p=self.transition_probs[current_state])
        return observations

# Ejemplo de uso
transition_probs = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
emission_probs = np.array([[0.9, 0.1], [0.2, 0.8]])  # Matriz de emisión
initial_probs = np.array([0.5, 0.5])  # Probabilidades iniciales de estado

hmm = HiddenMarkovModel(transition_probs, emission_probs, initial_probs)

# Generar una secuencia de observaciones de longitud 10
sequence = hmm.generate_sequence(10)
print("Secuencia de observaciones generada:", sequence)

