# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de lógica no monotónica en Python

# Definición de una base de conocimiento
class BaseConocimiento:
    def __init__(self):
        self.hechos = set()

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def eliminar_hecho(self, hecho):
        if hecho in self.hechos:
            self.hechos.remove(hecho)

# Definición de reglas
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def evaluar(self, base_conocimiento):
        if self.antecedente.issubset(base_conocimiento.hechos):
            base_conocimiento.eliminar_hecho(self.consecuente)

# Creación de una base de conocimiento y reglas
base_conocimiento = BaseConocimiento()
base_conocimiento.agregar_hecho("p")
regla_1 = Regla({"p"}, "q")

# Aplicación de las reglas
print("Hechos antes de aplicar la regla:", base_conocimiento.hechos)
regla_1.evaluar(base_conocimiento)
print("Hechos después de aplicar la regla:", base_conocimiento.hechos)
