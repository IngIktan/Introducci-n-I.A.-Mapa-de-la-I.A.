# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación de incertidumbre y factores de certeza utilizando probabilidad en Python

import random

class SistemaIncertidumbre:
    """Clase que simula un sistema con incertidumbre"""

    def __init__(self, probabilidad_alta):
        self.probabilidad_alta = probabilidad_alta

    def tomar_decision(self):
        """Simula la toma de decisión con incertidumbre"""
        if random.random() < self.probabilidad_alta:
            return "Decisión A (alta certeza)"
        else:
            return "Decisión B (baja certeza)"

if __name__ == "__main__":
    # Crear instancia del sistema con incertidumbre
    sistema = SistemaIncertidumbre(probabilidad_alta=0.7)

    # Simular toma de decisión
    decision = sistema.tomar_decision()
    print("Decisión:", decision)
