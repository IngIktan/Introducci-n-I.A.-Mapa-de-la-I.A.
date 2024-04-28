# Autor: Daniel Alejandro Flores Sepulveda
# Este programa verifica si una fórmula proposicional es una tautología.

from itertools import product

# Función para verificar si una fórmula proposicional es una tautología
def es_tautologia(formula):
    # Extraer las variables de la fórmula
    variables = set(caracter for caracter in formula if caracter.isalpha())
    
    # Generar todas las posibles asignaciones de valores a las variables
    asignaciones = product([True, False], repeat=len(variables))
    
    # Evaluar la fórmula para cada asignación de valores
    for asignacion in asignaciones:
        # Crear un diccionario de asignación de variables
        asignacion_dict = dict(zip(variables, asignacion))
        # Evaluar la fórmula con la asignación de variables
        if not eval(formula, asignacion_dict):
            return False  # Si la fórmula es falsa para alguna asignación, no es una tautología
    return True  # Si la fórmula es verdadera para todas las asignaciones, es una tautología

# Ejemplo de uso
if __name__ == "__main__":
    # Fórmula proposicional a verificar
    formula = "(p and q) or (not p and not q)"
    
    # Verificar si la fórmula es una tautología
    if es_tautologia(formula):
        print("La fórmula es una tautología.")
    else:
        print("La fórmula no es una tautología.")
