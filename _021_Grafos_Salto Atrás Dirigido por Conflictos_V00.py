# Daniel Alejandro Flores Sepulveda
# Implementación básica del Salto Atrás Dirigido por Conflictos para un problema de satisfacción de restricciones (CSP)

def salto_atras_dirigido_conflictos(estado, dominios, restricciones):
    asignaciones = {}  # Almacena las asignaciones realizadas durante la búsqueda
    while len(asignaciones) < len(estado):  # Mientras haya variables sin asignar
        variable, valor = seleccionar_variable_sin_asignar(estado, asignaciones, dominios)
        if variable is None:
            return None  # No se puede completar la asignación (falla)
        estado[variable] = valor  # Asignar el valor a la variable
        asignaciones[variable] = valor  # Registrar la asignación
        if not verificar_conflicto(estado, restricciones):
            conflicto = identificar_conflicto(estado, restricciones)
            if conflicto is None:
                continue
            variable_conflicto, valor_conflicto = conflicto
            asignaciones = retroceder(asignaciones, variable_conflicto)
            estado[variable] = valor_conflicto  # Retroceder y asignar valor conflictivo
    return asignaciones  # Solución encontrada

def seleccionar_variable_sin_asignar(estado, asignaciones, dominios):
    for variable, valor in estado.items():
        if valor is None and variable not in asignaciones:
            for val in dominios[variable]:
                return variable, val
    return None, None

def verificar_conflicto(estado, restricciones):
    for restriccion in restricciones:
        var1, var2 = restriccion
        if estado[var1] is not None and estado[var2] is not None and estado[var1] == estado[var2]:
            return True  # Se encontró un conflicto
    return False

def identificar_conflicto(estado, restricciones):
    for restriccion in restricciones:
        var1, var2 = restriccion
        if estado[var1] is not None and estado[var2] is not None and estado[var1] == estado[var2]:
            return var1, estado[var1]  # Variable y valor que causan el conflicto
    return None

def retroceder(asignaciones, variable_conflicto):
    nuevas_asignaciones = {}
    for variable, valor in asignaciones.items():
        if variable != variable_conflicto:
            nuevas_asignaciones[variable] = valor
    return nuevas_asignaciones

# Ejemplo de uso
estado = {'A': None, 'B': None, 'C': None}  # Estado inicial de las variables
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}  # Dominios de las variables
restricciones = [('A', 'B'), ('B', 'C')]  # Restricciones entre las variables

# Aplicar el Salto Atrás Dirigido por Conflictos para resolver el CSP
solucion = salto_atras_dirigido_conflictos(estado, dominios, restricciones)

# Mostrar la solución encontrada (asignaciones)
print("Solución encontrada:")
print(solucion)
