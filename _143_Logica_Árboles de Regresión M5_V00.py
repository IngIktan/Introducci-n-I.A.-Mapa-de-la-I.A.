import numpy as np

def calcular_error_promedio(y):
    return np.mean(np.abs(y - np.mean(y)))

def calcular_ganancia(X, y, atributo, umbral):
    indices_izquierda = np.where(X[:, atributo] <= umbral)[0]
    indices_derecha = np.where(X[:, atributo] > umbral)[0]
    
    y_izquierda = y[indices_izquierda]
    y_derecha = y[indices_derecha]
    
    error_total = calcular_error_promedio(y)
    error_izquierda = calcular_error_promedio(y_izquierda)
    error_derecha = calcular_error_promedio(y_derecha)
    
    ganancia = error_total - (len(indices_izquierda) / len(y)) * error_izquierda \
              - (len(indices_derecha) / len(y)) * error_derecha
    return ganancia

def encontrar_mejor_division(X, y):
    mejor_ganancia = 0
    mejor_atributo = None
    mejor_umbral = None
    
    for atributo in range(X.shape[1]):
        valores_unicos = np.unique(X[:, atributo])
        for umbral in valores_unicos:
            ganancia = calcular_ganancia(X, y, atributo, umbral)
            if ganancia > mejor_ganancia:
                mejor_ganancia = ganancia
                mejor_atributo = atributo
                mejor_umbral = umbral
                
    return mejor_atributo, mejor_umbral

def construir_arbol(X, y, min_muestras_por_hoja):
    if len(y) <= min_muestras_por_hoja or len(np.unique(y)) == 1:
        return np.mean(y)
    
    mejor_atributo, mejor_umbral = encontrar_mejor_division(X, y)
    
    if mejor_atributo is None:
        return np.mean(y)
    
    indices_izquierda = np.where(X[:, mejor_atributo] <= mejor_umbral)[0]
    indices_derecha = np.where(X[:, mejor_atributo] > mejor_umbral)[0]
    
    X_izquierda, y_izquierda = X[indices_izquierda], y[indices_izquierda]
    X_derecha, y_derecha = X[indices_derecha], y[indices_derecha]
    
    arbol = {}
    arbol['atributo'] = mejor_atributo
    arbol['umbral'] = mejor_umbral
    arbol['izquierda'] = construir_arbol(X_izquierda, y_izquierda, min_muestras_por_hoja)
    arbol['derecha'] = construir_arbol(X_derecha, y_derecha, min_muestras_por_hoja)
    
    return arbol

# Ejemplo de uso
X = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([1, 2, 3, 4, 5])

arbol = construir_arbol(X, y, min_muestras_por_hoja=1)
print(arbol)
