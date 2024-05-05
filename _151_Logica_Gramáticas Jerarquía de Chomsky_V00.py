# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de definición de gramática y clasificación según la jerarquía de Chomsky.

class GramaticaChomsky:
    def __init__(self, reglas):
        self.reglas = reglas

    def clasificar(self):
        tipo = None
        for regla in self.reglas:
            partes = regla.split("->")
            izquierda = partes[0].strip()
            derecha = partes[1].strip()
            if len(derecha) == 1 and derecha.islower():
                if izquierda.isupper():
                    tipo = "Tipo 3 (Regular)"
                else:
                    tipo = "No Chomsky"
            elif len(derecha) == 2 and derecha[0].isupper() and derecha[1].islower():
                if izquierda.isupper():
                    tipo = "Tipo 2 (Libre de Contexto)"
                else:
                    tipo = "No Chomsky"
            elif len(derecha) == 2 and derecha[0].islower() and derecha[1].isupper():
                if izquierda.isupper():
                    tipo = "Tipo 1 (Sensible al Contexto)"
                else:
                    tipo = "No Chomsky"
            elif len(derecha) == 0:
                if izquierda.isupper():
                    tipo = "Tipo 0 (Irrestringida)"
                else:
                    tipo = "No Chomsky"
            else:
                tipo = "No Chomsky"
                break
        return tipo

# Definición de la gramática
reglas_gramatica = [
    "S -> AB",
    "A -> aA | a",
    "B -> b"
]

# Creación de la gramática
gramatica = GramaticaChomsky(reglas_gramatica)

# Clasificación de la gramática
tipo_gramatica = gramatica.clasificar()
print("Clasificación de la gramática según la jerarquía de Chomsky:", tipo_gramatica)
