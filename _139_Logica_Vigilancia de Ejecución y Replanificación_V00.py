# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de Vigilancia de Ejecución y Replanificación en Python

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

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

    def replan(self):
        print("Replanificando...")
        for task in self.tasks_in_progress:
            print(f"Replanificando tarea '{task.name}'...")
            # Aquí se implementaría la lógica para replanificar la tarea, por ejemplo, asignarle una nueva duración

# Crear algunas tareas
task1 = Task("Tarea 1", 3)
task2 = Task("Tarea 2", 5)
task3 = Task("Tarea 3", 7)

# Crear un monitor de ejecución
monitor = ExecutionMonitor()

# Iniciar la ejecución de las tareas
monitor.start_execution(task1)
monitor.start_execution(task2)
monitor.start_execution(task3)

# Simular la ejecución y revisar el estado periódicamente
for _ in range(10):
    print("----------")
    monitor.check_execution()
    if task2.duration == 3:  # Simulación de un cambio que requiere replanificación
        monitor.replan()
    for task in monitor.tasks_in_progress:
        task.duration -= 1
