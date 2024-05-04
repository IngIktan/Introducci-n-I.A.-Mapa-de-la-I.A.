# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de Redes Jerárquicas de Tareas en Python

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)

def calculate_duration(task):
    if not task.dependencies:
        return task.duration
    else:
        max_dependency_duration = max(calculate_duration(dep) for dep in task.dependencies)
        return task.duration + max_dependency_duration

# Crear las tareas
task1 = Task("Tarea 1", 5)
task2 = Task("Tarea 2", 8)
task3 = Task("Tarea 3", 6)
task4 = Task("Tarea 4", 7)

# Definir las dependencias
task2.add_dependency(task1)
task3.add_dependency(task1)
task4.add_dependency(task2)
task4.add_dependency(task3)

# Calcular la duración total
total_duration = calculate_duration(task4)
print("Duración total de la red de tareas:", total_duration)
