# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de un modelo probabilista racional en Python

class ModeloProbabilistaRacional:
    """Clase que define un modelo probabilista racional"""

    def __init__(self, creencias, acciones, utilidades):
        self.creencias = creencias
        self.acciones = acciones
        self.utilidades = utilidades

    def tomar_decision(self):
        """Función para tomar una decisión basada en el modelo probabilista racional"""

        mejor_accion = None
        mejor_utilidad = float("-inf")

        # Iterar sobre todas las acciones y calcular la utilidad esperada
        for accion in self.acciones:
            utilidad_esperada = sum(probabilidad * utilidad for probabilidad, utilidad in zip(self.creencias, self.utilidades[accion]))
            if utilidad_esperada > mejor_utilidad:
                mejor_accion = accion
                mejor_utilidad = utilidad_esperada

        return mejor_accion

if __name__ == "__main__":
    # Definir las creencias probabilísticas sobre el mundo
    creencias = [0.3, 0.5, 0.2]  # Por ejemplo, las creencias pueden representar las probabilidades de diferentes estados del mundo

    # Definir las posibles acciones
    acciones = ["A", "B", "C"]

    # Definir las utilidades de cada acción para cada estado del mundo
    utilidades = {
        "A": [10, 5, 0],  # Utilidades para la acción A en cada estado del mundo
        "B": [8, 6, 2],   # Utilidades para la acción B en cada estado del mundo
        "C": [3, 7, 9]    # Utilidades para la acción C en cada estado del mundo
    }

    # Crear instancia del modelo probabilista racional
    modelo = ModeloProbabilistaRacional(creencias, acciones, utilidades)

    # Tomar una decisión basada en el modelo
    decision = modelo.tomar_decision()

    # Imprimir la decisión tomada
    print("La decisión tomada es:", decision)
