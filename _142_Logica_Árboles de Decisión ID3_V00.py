# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación del algoritmo ID3 para árboles de decisión

import numpy as np

class NodoArbol:
    def __init__(self, valor=None, atributo=None, hijos=None):
        self.valor = valor
        self.atributo = atributo
        self.hijos = hijos if hijos else []

def entropia(clases):
    n = len(clases)
    clases_unicas = np.unique(clases)
    ent = 0
    for c in clases_unicas:
        prob = np.sum(clases == c) / n
        ent -= prob * np.log2(prob)
    return ent

def ganancia(X, y, atributo):
    ent_total = entropia(y)
    valores_atributo = np.unique(X[:, atributo])
    gan = ent_total
    for val in valores_atributo:
        indices = np.where(X[:, atributo] == val)[0]
        suby = y[indices]
        gan -= (len(indices) / len(y)) * entropia(suby)
    return gan

def id3(X, y, atributos):
    if len(np.unique(y)) == 1:  # Si todos los ejemplos son de la misma clase
        return NodoArbol(valor=y[0])
    if len(atributos) == 0:  # Si no quedan atributos para dividir
        clases, conteo_clases = np.unique(y, return_counts=True)
        return NodoArbol(valor=clases[np.argmax(conteo_clases)])
    
    ganancias = [ganancia(X, y, a) for a in atributos]
    mejor_atributo = atributos[np.argmax(ganancias)]
    
    nodo = NodoArbol(atributo=mejor_atributo)
    valores_atributo = np.unique(X[:, mejor_atributo])
    for val in valores_atributo:
        indices = np.where(X[:, mejor_atributo] == val)[0]
        subX = np.delete(X[indices], mejor_atributo, axis=1)
        suby = y[indices]
        if len(subX) == 0:
            clases, conteo_clases = np.unique(suby, return_counts=True)
            nodo.hijos.append(NodoArbol(valor=clases[np.argmax(conteo_clases)]))
        else:
            sub_atributos = [a for a in atributos if a != mejor_atributo]
            hijo = id3(subX, suby, sub_atributos)
            nodo.hijos.append(hijo)
    return nodo

# Ejemplo de uso
X = np.array([[1, 'sol'], [1, 'nublado'], [0, 'nublado'], [0, 'lluvia'], [0, 'lluvia']])
y = np.array(['si', 'no', 'si', 'si', 'no'])
atributos = [0, 1]  # Índices de los atributos en X

arbol = id3(X, y, atributos)
