# Daniel Alejandro Flores Sepulveda
# Implementación del algoritmo de Búsqueda Local: Mínimos Conflictos para resolver un Sudoku

import random

def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(" ".join(map(str, fila)))

def es_numero_valido(sudoku, numero, fila, columna):
    # Verificar si el número está en la fila
    if numero in sudoku[fila]:
        return False
    # Verificar si el número está en la columna
    for i in range(9):
        if sudoku[i][columna] == numero:
            return False
    # Verificar si el número está en el cuadrante 3x3
    cuadrante_fila_inicio, cuadrante_columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(cuadrante_fila_inicio, cuadrante_fila_inicio + 3):
        for j in range(cuadrante_columna_inicio, cuadrante_columna_inicio + 3):
            if sudoku[i][j] == numero:
                return False
    return True

def obtener_celdas_vacias(sudoku):
    celdas_vacias = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                celdas_vacias.append((i, j))
    return celdas_vacias

def minimos_conflictos(sudoku):
    max_iteraciones = 1000
    iteracion = 0
    while not es_sudoku_resuelto(sudoku) and iteracion < max_iteraciones:
        celdas_vacias = obtener_celdas_vacias(sudoku)
        fila, columna = random.choice(celdas_vacias)
        valores_posibles = [num for num in range(1, 10) if es_numero_valido(sudoku, num, fila, columna)]
        if valores_posibles:
            sudoku[fila][columna] = random.choice(valores_posibles)
        iteracion += 1
    return sudoku

def es_sudoku_resuelto(sudoku):
    for fila in sudoku:
        if 0 in fila:
            return False
    return True

# Ejemplo de uso
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku inicial:")
imprimir_sudoku(sudoku)

sudoku_resuelto = minimos_conflictos(sudoku)

print("\nSudoku resuelto:")
imprimir_sudoku(sudoku_resuelto)
