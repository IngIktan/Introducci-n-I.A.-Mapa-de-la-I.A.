# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo simple en Python que muestra cómo estructurar la explicación de un concepto y proporcionar información relevante.
# El código define una clase Explanation que tiene un atributo para el concepto y otro para los detalles.
# Luego, se crea una instancia de esta clase con el concepto "Redes Neuronales" y algunos detalles sobre ellas.
# Finalmente, se muestra la explicación utilizando el método display_explanation().

class Explanation:
    def __init__(self, concept, details):
        self.concept = concept
        self.details = details

    def display_explanation(self):
        print("Concept: ", self.concept)
        print("Details: ", self.details)


# Ejemplo de uso
concept = "Redes Neuronales"
details = "Las redes neuronales son modelos de aprendizaje computacional inspirados en el funcionamiento del cerebro humano. " \
          "Están compuestas por capas de neuronas interconectadas que procesan la información de entrada y generan una salida. " \
          "Las redes neuronales pueden utilizarse para una variedad de tareas, como reconocimiento de patrones, clasificación, " \
          "regresión y generación de texto, entre otras."

explanation = Explanation(concept, details)
explanation.display_explanation()
