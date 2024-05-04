# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de Planificación Condicional en Python

class ConditionalTask:
    def __init__(self, name, conditions, duration):
        self.name = name
        self.conditions = conditions
        self.duration = duration
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)

def calculate_duration(task, conditions):
    if not task.dependencies:
        return task.duration
    else:
        max_dependency_duration = max(calculate_duration(dep, conditions) for dep in task.dependencies)
        if all(condition in conditions for condition in task.conditions):
            return task.duration + max_dependency_duration
        else:
            return 0

# Crear las tareas condicionales
task1 = ConditionalTask("Tarea 1", ["condición1"], 5)
task2 = ConditionalTask("Tarea 2", ["condición2"], 8)
task3 = ConditionalTask("Tarea 3", ["condición3"], 6)
task4 = ConditionalTask("Tarea 4", ["condición1", "condición2"], 7)

# Definir las dependencias
task2.add_dependency(task1)
task3.add_dependency(task1)
task4.add_dependency(task2)
task4.add_dependency(task3)

# Definir las condiciones
conditions = ["condición1", "condición2"]

# Calcular la duración total considerando las condiciones
total_duration = calculate_duration(task4, conditions)
print("Duración total de la planificación condicional:", total_duration)
