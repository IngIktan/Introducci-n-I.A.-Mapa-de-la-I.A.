import numpy as np

# Entorno simple
class Environment:
    def __init__(self):
        self.n_actions = 2
        self.true_action_value = [0.1, 0.5]  # Valores verdaderos de las acciones

    def step(self, action):
        # Simular el resultado de tomar una acción
        reward = np.random.normal(self.true_action_value[action], 1)  # Recompensa con ruido gaussiano
        return reward

# Agente que utiliza la estrategia epsilon-greedy
class EpsilonGreedyAgent:
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.Q_values = [0, 0]  # Valores iniciales de las acciones
        self.action_counts = [0, 0]  # Contadores de las veces que se selecciona cada acción

    def select_action(self):
        # Selección de acción utilizando la estrategia epsilon-greedy
        if np.random.rand() < self.epsilon:  # Exploración
            return np.random.choice(len(self.Q_values))
        else:  # Explotación
            return np.argmax(self.Q_values)

    def update_Q_values(self, action, reward):
        # Actualización de los valores Q basada en la recompensa recibida
        self.action_counts[action] += 1
        self.Q_values[action] += (1 / self.action_counts[action]) * (reward - self.Q_values[action])

# Función principal
def main():
    env = Environment()
    agent = EpsilonGreedyAgent(epsilon=0.1)  # Agente con epsilon=0.1 para un 10% de exploración

    # Ejecución de episodios de interacción
    n_episodes = 1000
    total_rewards = 0
    for episode in range(n_episodes):
        action = agent.select_action()  # Selección de acción
        reward = env.step(action)  # Ejecución de la acción en el entorno
        agent.update_Q_values(action, reward)  # Actualización de los valores Q del agente
        total_rewards += reward

    print("Recompensa promedio obtenida:", total_rewards / n_episodes)

if __name__ == "__main__":
    main()
