# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de lógica modal en Python

# Definición de una estructura de mundo posible
class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proposiciones = set()

    def agregar_proposicion(self, proposicion):
        self.proposiciones.add(proposicion)

    def __str__(self):
        return self.nombre

# Definición de una fórmula modal básica
class FormulaModal:
    def __init__(self, mundo, proposicion):
        self.mundo = mundo
        self.proposicion = proposicion

    def evaluar(self):
        return self.proposicion in self.mundo.proposiciones

# Creación de mundos posibles
mundo1 = Mundo("Mundo1")
mundo1.agregar_proposicion("p")
mundo1.agregar_proposicion("q")

mundo2 = Mundo("Mundo2")
mundo2.agregar_proposicion("q")

# Creación de fórmulas modales
formula1 = FormulaModal(mundo1, "p")
formula2 = FormulaModal(mundo2, "p")

# Evaluación de las fórmulas modales
print("La fórmula 'p' es verdadera")
