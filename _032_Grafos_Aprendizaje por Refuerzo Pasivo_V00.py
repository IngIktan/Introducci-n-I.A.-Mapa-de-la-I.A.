# Daniel Alejandro Flores Sepulveda
# Implementación básica de Aprendizaje por Refuerzo Pasivo

import numpy as np

# Definir el entorno
class Environment:
    def __init__(self, n_states):
        self.n_states = n_states

    def step(self, action):
        # Aquí definimos las transiciones del estado actual al siguiente estado
        # y la recompensa correspondiente
        next_state = (action + 1) % self.n_states  # Siguiente estado después de la acción
        reward = 1 if next_state == 0 else 0  # Recompensa si llegamos al estado objetivo (0)
        return next_state, reward

# Agente que realiza aprendizaje por refuerzo pasivo
class PassiveRLAgent:
    def __init__(self, n_states, learning_rate):
        self.n_states = n_states
        self.value_function = np.zeros(n_states)  # Función de valor inicializada a 0
        self.learning_rate = learning_rate

    def update_value_function(self, state, reward):
        # Actualizar la función de valor mediante promedio ponderado
        self.value_function[state] += self.learning_rate * (reward - self.value_function[state])

# Configuración del entorno y el agente
n_states = 10  # Número de estados en el entorno
learning_rate = 0.1  # Tasa de aprendizaje del agente
env = Environment(n_states)
agent = PassiveRLAgent(n_states, learning_rate)

# Ejecutar episodios de interacción entre el agente y el entorno
n_episodes = 1000  # Número de episodios
for episode in range(n_episodes):
    state = 0  # Estado inicial
    while state != n_states - 1:  # Continuar hasta llegar al estado objetivo
        next_state, reward = env.step(state)
        agent.update_value_function(state, reward)
        state = next_state

# Mostrar la función de valor aprendida por el agente
print("Función de Valor Aprendida:")
print(agent.value_function)
