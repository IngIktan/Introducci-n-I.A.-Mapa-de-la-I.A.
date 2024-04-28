# Autor: Daniel Alejandro Flores Sepulveda
# Este programa utiliza resolución y forma normal conjuntiva (FNC) en lógica proposicional.

from sympy import symbols, Or, Not, to_cnf

# Función para aplicar resolución a dos cláusulas
def resolver(clausula1, clausula2):
    resolvente = Or(clausula1, clausula2)
    return resolvente.simplify()

# Función para convertir una fórmula a forma normal conjuntiva (FNC)
def a_fnc(formula):
    return to_cnf(Or(Not(formula.args[0]), formula.args[1]))

# Ejemplo de uso
if __name__ == "__main__":
    # Definir variables proposicionales
    p, q, r = symbols('p q r')

    # Ejemplo de cláusulas
    clausula1 = Or(p, q)
    clausula2 = Or(Not(p), r)

    # Aplicar resolución a las cláusulas
    resolvente = resolver(clausula1, clausula2)
    print("Resolvente:", resolvente)

    # Ejemplo de fórmula implicativa
    formula = p >> q

    # Convertir la fórmula a FNC
    fnc = a_fnc(formula)
    print("FNC de la fórmula:", fnc)
