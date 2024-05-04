# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de Planificación Continua y Multiagente en Python

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Agent:
    def __init__(self, name):
        self.name = name

class ExecutionMonitor:
    def __init__(self):
        self.tasks_in_progress = []

    def start_execution(self, task):
        self.tasks_in_progress.append(task)
        print(f"Tarea '{task.name}' en progreso...")

    def check_execution(self):
        for task in self.tasks_in_progress:
            print(f"Revisando estado de la tarea '{task.name}'...")
            if task.duration == 0:
                print(f"Tarea '{task.name}' completada.")
                self.tasks_in_progress.remove(task)
            else:
                print(f"Tarea '{task.name}' aún en progreso.")

class Planner:
    def __init__(self, agents):
        self.agents = agents

    def assign_task(self, task):
        print(f"Asignando tarea '{task.name}' a los agentes...")
        for agent in self.agents:
            print(f"Tarea '{task.name}' asignada al agente '{agent.name}'.")

# Crear algunos agentes y tareas
agent1 = Agent("Agente 1")
agent2 = Agent("Agente 2")
task1 = Task("Tarea 1", 3)
task2 = Task("Tarea 2", 5)

# Crear un monitor de ejecución
monitor = ExecutionMonitor()

# Crear un planificador y asignar tareas a los agentes
planner = Planner([agent1, agent2])
planner.assign_task(task1)
planner.assign_task(task2)

# Simular la ejecución y revisar el estado periódicamente
for _ in range(10):
    print("----------")
    monitor.check_execution()
    for task in monitor.tasks_in_progress:
        task.duration -= 1
