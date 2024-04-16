# Daniel Alejandro Flores Sepulveda
# Implementación básica de Busqueda de la politica 
import numpy as np

# Definición del entorno (en este ejemplo, un entorno de cuadrícula)
n_rows = 3
n_cols = 3
n_actions = 4  # 4 acciones posibles: arriba, abajo, izquierda, derecha
n_states = n_rows * n_cols  # Número total de estados

# Matriz de recompensas (recompensa -1 en todos los estados, excepto en el estado objetivo)
reward_matrix = np.full((n_rows, n_cols), -1)
reward_matrix[0, 2] = 10  # Estado objetivo con recompensa 10

# Definición de la función de transición de estado según la acción (determinística)
def transition_function(state, action):
    row, col = state // n_cols, state % n_cols  # Convertir estado en coordenadas de fila y columna
    if action == 0:  # Arriba
        row = max(0, row - 1)
    elif action == 1:  # Abajo
        row = min(n_rows - 1, row + 1)
    elif action == 2:  # Izquierda
        col = max(0, col - 1)
    elif action == 3:  # Derecha
        col = min(n_cols - 1, col + 1)
    return row * n_cols + col  # Convertir coordenadas de fila y columna en estado

# Algoritmo de iteración de política
def policy_iteration():
    # Inicializar política aleatoria
    policy = np.random.randint(0, n_actions, size=n_states)
    
    # Iteración de política
    max_iterations = 100
    for _ in range(max_iterations):
        # Evaluación de política
        V = np.zeros(n_states)  # Valores de estado inicializados a cero
        for s in range(n_states):
            next_state = transition_function(s, policy[s])
            V[s] = reward_matrix.flatten()[s] + V[next_state]  # Valor de estado = recompensa + valor del próximo estado (sin descuento)
        
        # Mejora de política
        new_policy = np.zeros_like(policy)
        for s in range(n_states):
            action_values = [reward_matrix.flatten()[s] + V[transition_function(s, a)] for a in range(n_actions)]
            new_policy[s] = np.argmax(action_values)
        
        # Comprobar si la política convergió
        if np.array_equal(policy, new_policy):
            break
        
        policy = new_policy
    
    return policy

# Ejecutar iteración de política y mostrar la política óptima resultante
optimal_policy = policy_iteration()
print("Política óptima:")
print(optimal_policy.reshape(n_rows, n_cols))
