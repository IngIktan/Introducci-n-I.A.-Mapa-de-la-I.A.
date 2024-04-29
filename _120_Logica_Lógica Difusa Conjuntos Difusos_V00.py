# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de conjuntos difusos en Python

class ConjuntoDifuso:
    def __init__(self, nombre, funcion_membresia):
        self.nombre = nombre
        self.funcion_membresia = funcion_membresia

    def grado_pertenencia(self, elemento):
        return self.funcion_membresia(elemento)

# Funciones de membresía para conjuntos difusos
def funcion_membresia_baja(x):
    if x < 20:
        return 1.0
    elif x >= 20 and x <= 40:
        return (40 - x) / 20.0
    else:
        return 0.0

def funcion_membresia_media(x):
    if x >= 20 and x <= 40:
        return (x - 20) / 20.0
    elif x > 40 and x < 60:
        return 1.0
    elif x >= 60 and x <= 80:
        return (80 - x) / 20.0
    else:
        return 0.0

def funcion_membresia_alta(x):
    if x >= 60:
        return 1.0
    elif x > 40 and x < 60:
        return (x - 40) / 20.0
    else:
        return 0.0

# Definición de conjuntos difusos
bajo = ConjuntoDifuso("Bajo", funcion_membresia_baja)
medio = ConjuntoDifuso("Medio", funcion_membresia_media)
alto = ConjuntoDifuso("Alto", funcion_membresia_alta)

# Ejemplo de cálculo del grado de pertenencia
temperatura = 35
print("Grado de pertenencia de", temperatura, "en el conjunto difuso 'Medio':", medio.grado_pertenencia(temperatura))
