# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de una gramática causal definida en Python.

class GramaticaCausalDefinida:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, causa, efecto):
        self.reglas.append((causa, efecto))

    def verificar_causa(self, causa):
        for regla in self.reglas:
            if regla[0] == causa:
                return regla[1]
        return None

# Crear una instancia de la gramática causal definida
gramatica = GramaticaCausalDefinida()

# Agregar algunas reglas
gramatica.agregar_regla("lluvia", "crecimiento de plantas")
gramatica.agregar_regla("fertilizante", "crecimiento de plantas")
gramatica.agregar_regla("sequía", "muerte de plantas")

# Verificar algunas causas y sus efectos
causa = "lluvia"
efecto = gramatica.verificar_causa(causa)
print(f"La causa '{causa}' produce el efecto '{efecto}'")

causa = "fertilizante"
efecto = gramatica.verificar_causa(causa)
print(f"La causa '{causa}' produce el efecto '{efecto}'")

causa = "sequía"
efecto = gramatica.verificar_causa(causa)
print(f"La causa '{causa}' produce el efecto '{efecto}' si no hay riego")
