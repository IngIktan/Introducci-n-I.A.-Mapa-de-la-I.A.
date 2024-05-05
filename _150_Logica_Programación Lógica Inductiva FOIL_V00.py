# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo básico de Programación Lógica Inductiva con el algoritmo FOIL.

class FOIL:
    def __init__(self, positive_examples, negative_examples):
        self.positive_examples = positive_examples
        self.negative_examples = negative_examples
        self.predicate = None

    def learn(self):
        # Ejemplo simple de FOIL
        self.predicate = "HasFeature(X, feature)"  # Predicado a aprender
        return self.predicate

# Ejemplo de uso
positive_examples = ["perro", "gato", "conejo"]
negative_examples = ["árbol", "coche", "mesa"]

foil = FOIL(positive_examples, negative_examples)
learned_predicate = foil.learn()
print("Predicado aprendido:", learned_predicate)
