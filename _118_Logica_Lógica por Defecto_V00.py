# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de lógica por defecto en Python

# Definición de una base de conocimiento por defecto
class BaseConocimientoPorDefecto:
    def __init__(self):
        self.afirmaciones = set()
        self.default_rules = set()

    def agregar_afirmacion(self, afirmacion):
        self.afirmaciones.add(afirmacion)

    def agregar_regla_por_defecto(self, regla):
        self.default_rules.add(regla)

    def inferir(self, query):
        for regla in self.default_rules:
            if regla.aplicar(self.afirmaciones, query):
                return True
        return False

# Definición de una regla por defecto
class ReglaPorDefecto:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def aplicar(self, afirmaciones, query):
        if self.antecedente.issubset(afirmaciones) and self.consecuente == query:
            return True
        return False

# Creación de una base de conocimiento por defecto y reglas
base_por_defecto = BaseConocimientoPorDefecto()
base_por_defecto.agregar_afirmacion("p")
regla_por_defecto = ReglaPorDefecto({"p"}, "q")

# Inferencia en la base de conocimiento por defecto
print("¿q se infiere por defecto?", base_por_defecto.inferir("q"))
