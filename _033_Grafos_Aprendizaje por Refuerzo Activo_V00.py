# Daniel Alejandro Flores Sepulveda
# Implementación básica de Aprendizaje por Refuerzo Activo (Q-learning)

import numpy as np

# Definir el entorno
class Environment:
    def __init__(self, n_states, n_actions):
        self.n_states = n_states
        self.n_actions = n_actions
        self.Q_values = np.zeros((n_states, n_actions))  # Valores Q inicializados a 0
        self.transition_matrix = self.generate_transition_matrix(n_states, n_actions)

    def generate_transition_matrix(self, n_states, n_actions):
        # Generar una matriz de transición aleatoria y normalizar las filas
        transition_matrix = np.random.rand(n_states, n_actions, n_states)
        for i in range(n_states):
            for j in range(n_actions):
                transition_matrix[i, j] /= np.sum(transition_matrix[i, j])  # Normalizar la fila
        return transition_matrix

    def step(self, state, action):
        # Simular el siguiente estado y la recompensa correspondiente
        next_state = np.random.choice(self.n_states, p=self.transition_matrix[state, action])
        reward = 1 if next_state == self.n_states - 1 else 0  # Recompensa si llegamos al estado objetivo
        return next_state, reward

# Agente que realiza aprendizaje por refuerzo activo (Q-learning)
class ActiveRLAgent:
    def __init__(self, n_actions, learning_rate, discount_factor):
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def select_action(self, state, Q_values):
        # Selección de la acción utilizando una política epsilon-greedy
        if np.random.rand() < 0.1:  # Exploración (10% de las veces)
            return np.random.choice(self.n_actions)
        else:  # Explotación (90% de las veces)
            return np.argmax(Q_values[state])

    def update_Q_values(self, state, action, reward, next_state, Q_values):
        # Actualización de los valores Q utilizando el algoritmo Q-learning
        max_next_Q = np.max(Q_values[next_state])
        Q_values[state, action] += self.learning_rate * (reward + self.discount_factor * max_next_Q - Q_values[state, action])

# Configuración del entorno y el agente
n_states = 10  # Número de estados en el entorno
n_actions = 2  # Número de acciones posibles en cada estado
learning_rate = 0.1  # Tasa de aprendizaje del agente
discount_factor = 0.9  # Factor de descuento de recompensas futuras
env = Environment(n_states, n_actions)
agent = ActiveRLAgent(n_actions, learning_rate, discount_factor)

# Ejecutar episodios de interacción entre el agente y el entorno
n_episodes = 1000  # Número de episodios
for episode in range(n_episodes):
    state = 0  # Estado inicial
    while state != n_states - 1:  # Continuar hasta llegar al estado objetivo
        action = agent.select_action(state, env.Q_values)
        next_state, reward = env.step(state, action)
        agent.update_Q_values(state, action, reward, next_state, env.Q_values)
        state = next_state

# Mostrar los valores Q aprendidos por el agente
print("Valores Q Aprendidos:")
print(env.Q_values)
