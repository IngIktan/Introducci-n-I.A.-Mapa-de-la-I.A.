# Daniel Alejandro Flores Sepulveda
# Ejemplo básico de un CSP para colorear un mapa

# Definición de las variables (regiones del mapa)
regiones = ['A', 'B', 'C', 'D']

# Definición de los dominios (colores disponibles para cada región)
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde'],
    'C': ['verde', 'azul'],
    'D': ['rojo', 'azul']
}

# Definición de las restricciones (regiones adyacentes no pueden tener el mismo color)
restricciones = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'A'), ('B', 'C'), ('B', 'D'),
    ('C', 'A'), ('C', 'B'), ('C', 'D'),
    ('D', 'B'), ('D', 'C')
]

# Función para verificar si una asignación satisface todas las restricciones
def verificar_asignacion(asignacion):
    for reg1, reg2 in restricciones:
        if reg1 in asignacion and reg2 in asignacion and asignacion[reg1] == asignacion[reg2]:
            return False
    return True

# Función para resolver el CSP utilizando búsqueda con retroceso (backtracking)
def resolver_csp(asignacion, dominios):
    if len(asignacion) == len(regiones):
        return asignacion  # Todas las variables están asignadas, solución encontrada
    region_no_asignada = [r for r in regiones if r not in asignacion][0]  # Seleccionar una variable no asignada
    for valor in dominios[region_no_asignada]:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[region_no_asignada] = valor
        if verificar_asignacion(nueva_asignacion):
            resultado = resolver_csp(nueva_asignacion, dominios)
            if resultado is not None:
                return resultado
    return None  # No se encontró solución

# Resolver el CSP
asignacion_inicial = {}
solucion = resolver_csp(asignacion_inicial, dominios)

# Mostrar la solución
if solucion is not None:
    print("Solución encontrada:")
    for region, color in solucion.items():
        print(f"Región {region}: Color {color}")
else:
    print("No se encontró solución para el CSP.")
