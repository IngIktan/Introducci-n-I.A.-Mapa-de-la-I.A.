# Daniel Alejandro Flores Sepulveda
# Implementación básica de la comprobación hacia adelante para un problema de satisfacción de restricciones (CSP)

def comprobacion_hacia_adelante(estado, dominios, restricciones):
    cambios = True  # Variable para seguir realizando cambios en los dominios
    while cambios:
        cambios = False
        for variable in estado:
            for valor in dominios[variable][:]:
                estado[variable] = valor  # Asignar temporalmente el valor a la variable
                if not consistente(estado, restricciones):
                    dominios[variable].remove(valor)  # Eliminar el valor inconsistente del dominio
                    cambios = True  # Se realizó un cambio en los dominios
            estado[variable] = None  # Restablecer el valor de la variable a None
    return estado, dominios

def consistente(estado, restricciones):
    for r in restricciones:
        if r[0] in estado and r[1] in estado and estado[r[0]] == estado[r[1]]:
            return False  # Las restricciones no se satisfacen
    return True  # Todas las restricciones se satisfacen

# Ejemplo de uso
estado = {'A': None, 'B': None, 'C': None}  # Estado inicial de las variables
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}  # Dominios de las variables
restricciones = [('A', 'B'), ('B', 'C')]  # Restricciones entre las variables

# Aplicar comprobación hacia adelante para reducir los dominios
nuevo_estado, nuevos_dominios = comprobacion_hacia_adelante(estado, dominios, restricciones)

# Mostrar los dominios actualizados
print("Dominios actualizados después de la comprobación hacia adelante:")
print(nuevos_dominios)
