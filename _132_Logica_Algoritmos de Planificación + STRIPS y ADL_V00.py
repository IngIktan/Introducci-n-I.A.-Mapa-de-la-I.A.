# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica del algoritmo de planificación STRIPS en Python

class STRIPS:
    def __init__(self, init_state, goal_state, actions):
        self.init_state = init_state
        self.goal_state = goal_state
        self.actions = actions

    def plan(self):
        plan = []

        # Estado inicial
        state = self.init_state.copy()

        # Mientras no se haya alcanzado el estado objetivo
        while not self.is_goal_state(state):
            applicable_actions = self.get_applicable_actions(state)
            chosen_action = self.choose_action(applicable_actions)
            plan.append(chosen_action)
            state = self.apply_action(state, chosen_action)

        return plan

    def is_goal_state(self, state):
        return all(state[key] >= self.goal_state[key] for key in self.goal_state)

    def get_applicable_actions(self, state):
        return [action for action in self.actions if all(state[key] >= action.preconditions[key] for key in action.preconditions)]

    def choose_action(self, applicable_actions):
        # Simple strategy: choose the first applicable action
        return applicable_actions[0]

    def apply_action(self, state, action):
        new_state = state.copy()
        for key, value in action.effects.items():
            new_state[key] += value
        return new_state

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

if __name__ == "__main__":
    # Definir el estado inicial
    init_state = {"at_A": 1, "at_B": 0, "has_package": 0}

    # Definir el estado objetivo
    goal_state = {"at_A": 0, "at_B": 1, "has_package": 1}

    # Definir las acciones disponibles
    actions = [
        Action("move_A_to_B", {"at_A": 1}, {"at_A": -1, "at_B": 1}),
        Action("pickup_package", {"has_package": 0}, {"has_package": 1})
    ]

    # Crear instancia del planificador STRIPS
    planner = STRIPS(init_state, goal_state, actions)

    # Generar el plan
    plan = planner.plan()

    # Imprimir el plan
    print("Plan generado:")
    for action in plan:
        print(action.name)
