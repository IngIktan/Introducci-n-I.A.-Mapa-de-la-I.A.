# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de lógica temporal en Python

# Definición de una estructura de tiempo
class Tiempo:
    def __init__(self, instante):
        self.instante = instante
        self.proposiciones = set()

    def agregar_proposicion(self, proposicion):
        self.proposiciones.add(proposicion)

    def __str__(self):
        return str(self.instante)

# Definición de una fórmula temporal básica
class FormulaTemporal:
    def __init__(self, tiempo, proposicion):
        self.tiempo = tiempo
        self.proposicion = proposicion

    def evaluar(self):
        return self.proposicion in self.tiempo.proposiciones

# Creación de instantes de tiempo
tiempo1 = Tiempo(1)
tiempo1.agregar_proposicion("p")

tiempo2 = Tiempo(2)
tiempo2.agregar_proposicion("q")

# Creación de fórmulas temporales
formula1 = FormulaTemporal(tiempo1, "p")
formula2 = FormulaTemporal(tiempo2, "p")

# Evaluación de las fórmulas temporales
print("La fórmula 'p' es verdadera en el tiempo 1:", formula1.evaluar())
print("La fórmula 'p' es verdadera en el tiempo 2:", formula2.evaluar())
