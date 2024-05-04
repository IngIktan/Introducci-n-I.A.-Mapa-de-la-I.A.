# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de representación de reglas en Python

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def __str__(self):
        return f'Antecedente: {self.antecedente} => Consecuente: {self.consecuente}'

# Crear reglas
regla1 = Regla("si está lloviendo", "llevar un paraguas")
regla2 = Regla("si es de noche", "encender las luces")

# Imprimir reglas
print(regla1)
print(regla2)
