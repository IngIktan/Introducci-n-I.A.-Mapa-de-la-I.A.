# Daniel Alejandro Flores Sepulveda
# Programa para resolver un Sudoku utilizando el algoritmo de Backtracking

def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(" ".join(map(str, fila)))

def encontrar_celda_vacia(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None

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

def resolver_sudoku(sudoku):
    fila, columna = encontrar_celda_vacia(sudoku)
    if fila is None:
        return True  # Sudoku resuelto
    for numero in range(1, 10):
        if es_numero_valido(sudoku, numero, fila, columna):
            sudoku[fila][columna] = numero
            if resolver_sudoku(sudoku):
                return True
            sudoku[fila][columna] = 0  # Retroceder si no se encuentra solución
    return False

def ingresar_sudoku():
    sudoku = []
    print("Ingrese los números del sudoku, fila por fila:")
    for i in range(9):
        fila = list(map(int, input(f"Ingrese los números de la fila {i+1}, separados por espacio: ").split()))
        sudoku.append(fila)
    return sudoku

# Ejemplo de uso
print("Ingrese los números del Sudoku, columna por columna:")
sudoku = ingresar_sudoku()

if resolver_sudoku(sudoku):
    print("\nSudoku resuelto:")
    imprimir_sudoku(sudoku)
else:
    print("\nNo se encontró solución para el Sudoku ingresado.")
