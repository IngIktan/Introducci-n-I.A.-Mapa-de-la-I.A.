# Autor: Daniel Alejandro Flores Sepulveda
# Este programa implementa el algoritmo de backtracking para resolver el problema de las N reinas.

# Función para verificar si una reina puede ser colocada en la posición (fila, col) en el tablero
def es_seguro(tablero, fila, col, N):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # Verificar si hay una reina en la diagonal izquierda superior
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar si hay una reina en la diagonal derecha superior
    for i, j in zip(range(fila, -1, -1), range(col, N)):
        if tablero[i][j] == 1:
            return False

    return True

# Función auxiliar recursiva para colocar reinas en el tablero
def colocar_reinas_util(tablero, fila, N):
    # Caso base: todas las reinas están colocadas
    if fila >= N:
        return True

    # Probar colocar una reina en cada columna de la fila actual
    for col in range(N):
        if es_seguro(tablero, fila, col, N):
            # Colocar la reina en la posición (fila, col)
            tablero[fila][col] = 1

            # Recursivamente colocar el resto de las reinas
            if colocar_reinas_util(tablero, fila + 1, N):
                return True

            # Si no se puede colocar la reina en esta posición, retroceder (backtrack)
            tablero[fila][col] = 0

    # Si no se encuentra ninguna posición válida en esta fila, devolver False
    return False

# Función principal para resolver el problema de las N reinas
def resolver_n_reinas(N):
    # Inicializar el tablero con ceros
    tablero = [[0] * N for _ in range(N)]

    # Llamar a la función auxiliar para colocar las reinas
    if not colocar_reinas_util(tablero, 0, N):
        print("No hay solución para el problema de las", N, "reinas.")
        return False

    # Imprimir el tablero con las reinas colocadas
    print("Solución para el problema de las", N, "reinas:")
    for fila in tablero:
        print(' '.join(map(str, fila)))
    return True

# Ejemplo de uso
if __name__ == "__main__":
    N = 8  # Número de reinas
    resolver_n_reinas(N)
