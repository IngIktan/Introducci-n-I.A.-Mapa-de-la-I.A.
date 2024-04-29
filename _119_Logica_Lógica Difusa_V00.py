# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica de lógica difusa sin bibliotecas externas en Python

import numpy as np

# Funciones de membresía para la variable lingüística "temperatura"
def membresia_fria(x):
    return max(0, min((50 - x) / 50, 1))

def membresia_calida(x):
    return max(0, min(x / 50, 1))

# Reglas difusas para inferir la velocidad del ventilador
def regla_alta(temperatura):
    return membresia_fria(temperatura)

def regla_baja(temperatura):
    return membresia_calida(temperatura)

# Inferencia difusa
def inferencia_difusa(temperatura):
    velocidad_alta = regla_alta(temperatura)
    velocidad_baja = regla_baja(temperatura)

    # Defuzzificación (método simple: media ponderada)
    velocidad_ventilador = (velocidad_alta * 100 + velocidad_baja * 0) / (velocidad_alta + velocidad_baja)
    return velocidad_ventilador

# Ejemplo de inferencia difusa con una temperatura de 30 grados
temperatura_ambiente = 30
velocidad_resultante = inferencia_difusa(temperatura_ambiente)
print("Velocidad del ventilador:", velocidad_resultante)
