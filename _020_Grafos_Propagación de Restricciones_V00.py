# Daniel Alejandro Flores Sepulveda
# Implementación básica de la propagación de restricciones para un problema de satisfacción de restricciones (CSP)

def propagacion_restricciones(dominios, restricciones):
    cambios = True  # Variable para seguir realizando cambios en los dominios
    while cambios:
        cambios = False
        for restriccion in restricciones:
            variable1, variable2 = restriccion
            for valor1 in dominios[variable1][:]:
                if not any(es_consistente(valor1, valor2) for valor2 in dominios[variable2]):
                    dominios[variable1].remove(valor1)  # Eliminar valor inconsistente
                    cambios = True  # Se realizó un cambio en los dominios
    return dominios

def es_consistente(valor1, valor2):
    # Esta función verifica si dos valores son consistentes entre sí
    return valor1 != valor2  # Por ejemplo, dos valores diferentes son consistentes

# Ejemplo de uso
dominios = {'A': [1, 2, 3], 'B': [4, 2, 3], 'C': [1, 2, 3]}  # Dominios de las variables
restricciones = [('A', 'B'), ('B', 'C')]  # Restricciones entre las variables

# Aplicar propagación de restricciones para reducir los dominios
nuevos_dominios = propagacion_restricciones(dominios, restricciones)

# Mostrar los dominios actualizados
print("Dominios actualizados después de la propagación de restricciones:")
print(nuevos_dominios)

