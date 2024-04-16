# Daniel Alejandro Flores Sepulveda
# Programa en Python para ilustrar una función de utilidad simple

def funcion_utilidad(resultado):
    # Definición de una función de utilidad simple
    if resultado == "Éxito":
        utilidad = 10
    elif resultado == "Fracaso":
        utilidad = 0
    else:
        utilidad = 5
    return utilidad

# Ejemplo de uso
resultado_1 = "Éxito"
resultado_2 = "Fracaso"
resultado_3 = "Medio"
print("Utilidad de resultado 1:", funcion_utilidad(resultado_1))
print("Utilidad de resultado 2:", funcion_utilidad(resultado_2))
print("Utilidad de resultado 3:", funcion_utilidad(resultado_3))
