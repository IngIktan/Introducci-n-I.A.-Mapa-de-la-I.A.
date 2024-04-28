# Autor: Daniel Alejandro Flores Sepulveda
# Este programa proporciona funciones para verificar la equivalencia, validez y satisfacibilidad de fórmulas proposicionales.

from sympy.logic.boolalg import Implies
from sympy import symbols
from sympy.logic.inference import satisfiable

# Función para verificar la equivalencia entre dos fórmulas proposicionales
def verificar_equivalencia(formula1, formula2):
    return formula1 == formula2

# Función para verificar la validez de una fórmula proposicional
def verificar_validez(formula):
    return satisfiable(Implies(formula, True)) is None

# Función para verificar la satisfacibilidad de una fórmula proposicional
def verificar_satisfacibilidad(formula):
    return satisfiable(formula) is not None

# Ejemplo de uso
if __name__ == "__main__":
    # Definir variables proposicionales
    p, q = symbols('p q')

    # Ejemplo de fórmulas proposicionales
    formula1 = p | (~p & q)
    formula2 = (p | ~p) & (p | q)

    # Verificar la equivalencia entre formula1 y formula2
    if verificar_equivalencia(formula1, formula2):
        print("formula1 y formula2 son equivalentes.")
    else:
        print("formula1 y formula2 no son equivalentes.")

    # Verificar la validez de formula1
    if verificar_validez(formula1):
        print("formula1 es válida.")
    else:
        print("formula1 no es válida.")

    # Verificar la satisfacibilidad de formula2
    if verificar_satisfacibilidad(formula2):
        print("formula2 es satisfacible.")
    else:
        print("formula2 no es satisfacible.")
