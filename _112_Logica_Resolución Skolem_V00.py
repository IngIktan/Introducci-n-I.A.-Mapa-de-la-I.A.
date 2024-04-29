# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación corregida de resolución Skolem en Python

# Función para generar una nueva constante de Skolem
def generar_constante_skolem():
    # Podrías implementar una lógica más sofisticada para generar constantes de Skolem únicas
    return "s" + str(generar_constante_skolem.contador)
generar_constante_skolem.contador = 0

# Función para aplicar resolución Skolem a una fórmula existencial
def resolucion_skolem(formula):
    # Reemplazar cada cuantificador existencial con una nueva constante de Skolem
    # En este ejemplo, asumimos que la fórmula está en forma normal prenex
    nueva_formula = formula
    for i, subformula in enumerate(formula.split()):
        if subformula[0] == "E":
            nueva_constante_skolem = generar_constante_skolem()
            # Reemplazar el cuantificador existencial por universal
            nueva_formula = nueva_formula.replace(subformula[3:], nueva_constante_skolem)
            nueva_formula = nueva_formula.replace(subformula[0], "∀")  
    return nueva_formula

# Ejemplo de uso
if __name__ == "__main__":
    formula_existencial = "E x P(x)"
    print("Fórmula original:", formula_existencial)
    formula_sin_existentiales = resolucion_skolem(formula_existencial)
    print("Fórmula después de resolución Skolem:", formula_sin_existentiales)
