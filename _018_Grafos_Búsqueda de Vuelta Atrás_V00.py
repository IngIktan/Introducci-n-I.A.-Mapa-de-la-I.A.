# Daniel Alejandro Flores Sepulveda
# Algoritmo de Búsqueda de Vuelta Atrás para el problema de las N reinas

# Función para verificar si es seguro colocar una reina en una posición dada
def es_seguro(tablero, fila, columna):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False
    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila-1, -1, -1), range(columna-1, -1, -1)):
        if tablero[i] == j:
            return False
    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila-1, -1, -1), range(columna+1, len(tablero))):
        if tablero[i] == j:
            return False
    # Si no hay ninguna reina amenazando la posición, retornar True (es seguro)
    return True

# Función de ayuda recursiva para resolver el problema de las N reinas
def resolver_n_reinas_util(tablero, fila):
    # Caso base: si se han colocado todas las reinas, retornar True (se encontró una solución)
    if fila >= len(tablero):
        return True
    # Recorrer todas las columnas en la fila actual
    for columna in range(len(tablero)):
        # Verificar si es seguro colocar una reina en la posición actual
        if es_seguro(tablero, fila, columna):
            # Colocar una reina en la posición actual
            tablero[fila] = columna
            # Llamada recursiva para colocar la siguiente reina en la siguiente fila
            if resolver_n_reinas_util(tablero, fila + 1):
                return True  # Si se encontró una solución, retornar True
            tablero[fila] = -1  # Retroceder: quitar la reina de la posición actual
    return False  # Si no se encontró ninguna solución en esta rama, retornar False

# Función principal para resolver el problema de las N reinas
def resolver_n_reinas(n):
    # Crear un tablero inicializado con -1 (ninguna reina colocada)
    tablero = [-1] * n
    # Llamar a la función de ayuda para resolver el problema recursivamente
    if resolver_n_reinas_util(tablero, 0):
        print("Solución encontrada:")
        for fila in range(n):
            print(tablero[fila])  # Imprimir la posición de las reinas en cada fila
    else:
        print("No se encontró solución.")  # Si no se encontró ninguna solución, imprimir un mensaje

# Ejemplo de uso
n = 8  # Tamaño del tablero (n x n)
resolver_n_reinas(n)  # Resolver el problema de las N reinas para el tamaño dado
