# Autor: Daniel Alejandro Flores Sepulveda
# Ejemplo Logica con interferencia de unificacion

def unificacion(termino1, termino2, sustitucion={}):
    if sustitucion is None:  # Si no hay sustitución previa, inicializarla como un diccionario vacío
        sustitucion = {}

    if isinstance(termino1, str) and isinstance(termino2, str):  # Caso base: ambos términos son variables
        if termino1 in sustitucion:
            return unificacion(sustitucion[termino1], termino2, sustitucion)
        elif termino2 in sustitucion:
            return unificacion(termino1, sustitucion[termino2], sustitucion)
        elif termino1 == termino2:
            return sustitucion
        else:
            sustitucion[termino1] = termino2
            return sustitucion

    elif isinstance(termino1, list) and isinstance(termino2, list):  # Caso recursivo: ambos términos son listas
        if len(termino1) != len(termino2):
            return None  # Las listas tienen longitudes diferentes, no se pueden unificar
        else:
            for subterm1, subterm2 in zip(termino1, termino2):
                sustitucion = unificacion(subterm1, subterm2, sustitucion)
            return sustitucion

    else:  # Caso base: al menos uno de los términos es un átomo
        if termino1 == termino2:
            return sustitucion
        else:
            return None  # No se puede unificar

# Ejemplo de unificación
termino1 = ['f', 'X', 'Y']
termino2 = ['f', 'a', 'b']
sustitucion = unificacion(termino1, termino2)
print("Unificación:", sustitucion)
