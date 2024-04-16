# Daniel Alejandro Flores Sepulveda
# Programa para implementar el algoritmo Q-Learning para resolver un laberinto

import numpy as np

# Definir el entorno (laberinto)
class Environment:
    def __init__(self):
        self.grid = np.array([
            [0, 0, 0, 0, 0, 0],
            [0, -1, -1, -1, -1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, -1, -1, -1, -1, 0],
            [0, 0, 0, 0, 0, 0]
        ])  # 0 representa un espacio libre, -1 representa un obstáculo, 1 representa la meta
        self.n_rows, self.n_cols = self.grid.shape
        self.goal = (4, 5)  # La meta está en la posición (4, 5)

    def reset(self):
        # Reiniciar el estado del agente al inicio del laberinto
        return (0, 0)

    def step(self, state, action):
        # Simular un paso del agente en el entorno
        row, col = state
        if action == 0:  # Mover hacia arriba
            new_state = (max(row - 1, 0), col)
        elif action == 1:  # Mover hacia abajo
            new_state = (min(row + 1, self.n_rows - 1), col)
        elif action == 2:  # Mover hacia la izquierda
            new_state = (row, max(col - 1, 0))
        elif action == 3:  # Mover hacia la derecha
            new_state = (row, min(col + 1, self.n_cols - 1))

        reward = -1  # Penalizar cada paso
        if self.grid[new_state] == -1:  # Si el siguiente estado es un obstáculo, permanecer en el mismo estado
            new_state = state
        elif new_state == self.goal:  # Si se llega a la meta, dar una recompensa
            reward = 0

        return new_state, reward

# Implementación de Q-Learning
class QLearningAgent:
    def __init__(self, n_actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.Q_values = np.zeros((5, 6, n_actions))  # Inicializar los valores Q a 0

    def select_action(self, state):
        # Selección de la acción utilizando una política epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        else:
            return np.argmax(self.Q_values[state])

    def update_Q_values(self, state, action, reward, next_state):
        # Actualizar los valores Q utilizando la ecuación de Q-Learning
        max_next_Q = np.max(self.Q_values[next_state])
        self.Q_values[state][action] += self.learning_rate * (reward + self.discount_factor * max_next_Q - self.Q_values[state][action])

# Entrenamiento del agente Q-Learning para resolver el laberinto
env = Environment()
agent = QLearningAgent(n_actions=4)

n_episodes = 1000  # Número de episodios de entrenamiento
for episode in range(n_episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.select_action(state)
        next_state, reward = env.step(state, action)
        agent.update_Q_values(state, action, reward, next_state)
        state = next_state
        if state == env.goal:  # Si el agente llega a la meta, terminar el episodio
            done = True

# Evaluar el rendimiento del agente entrenado
state = env.reset()
done = False
while not done:
    action = agent.select_action(state)
    next_state, reward = env.step(state, action)
    state = next_state
    if state == env.goal:  # Si el agente llega a la meta, terminar la ejecución
        done = True

# Imprimir el laberinto con las rutas óptimas aprendidas por el agente
optimal_path = np.zeros((5, 6), dtype=int)
state = env.reset()
done = False
while not done:
    optimal_path[state] = 1
    action = agent.select_action(state)
    next_state, reward = env.step(state, action)
    state = next_state
    if state == env.goal:
        done = True
print("Laberinto con ruta óptima:")
print(optimal_path)
