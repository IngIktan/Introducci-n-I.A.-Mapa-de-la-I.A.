# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda Voraz (Primero el Mejor) en un grafo dado.

import heapq  # Importamos el módulo heapq para utilizar colas de prioridad.

# Definición de la función para la búsqueda Voraz (Primero el Mejor)
def busqueda_voraz_primero_el_mejor(grafo, inicio, objetivo, heuristica):
    camino = [inicio]  # Inicializamos el camino con el nodo inicial.
    costo_acumulado = 0  # Inicializamos el costo acumulado en 0.
    
    # Mientras el último nodo del camino no sea el objetivo.
    while camino[-1] != objetivo:
        nodo_actual = camino[-1]  # Obtenemos el nodo actual del camino.
        adyacentes = grafo[nodo_actual]  # Obtenemos los nodos adyacentes al nodo actual.
        
        # Calculamos el costo heurístico para cada nodo adyacente.
        costos_heuristicos = [(heuristica(nodo, objetivo), nodo) for nodo in adyacentes]
        
        # Seleccionamos el nodo adyacente con el menor costo heurístico.
        siguiente_nodo = min(costos_heuristicos)[1]
        
        # Agregamos el siguiente nodo al camino y actualizamos el costo acumulado.
        camino.append(siguiente_nodo)
        costo_acumulado += grafo[nodo_actual][siguiente_nodo]
    
    # Retornamos el camino y el costo acumulado.
    return camino, costo_acumulado

# Ejemplo de un grafo de ejemplo representado como un diccionario de diccionarios con los costos de las aristas.
grafo = {
    'A': {'B': 5, 'C': 7},
    'B': {'A': 5, 'D': 3, 'E': 4},
    'C': {'A': 7, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 4, 'F': 6},
    'F': {'C': 2, 'E': 6}
}

# Función heurística para estimar la distancia entre dos nodos en el grafo.
def heuristica_distancia(nodo_actual, objetivo):
    # Aquí podrías implementar tu propia heurística que estime la distancia entre los nodos.
    pass

# Definir el nodo inicial y el nodo objetivo para la búsqueda.
inicio = 'A'
objetivo = 'F'

# Utilizamos la búsqueda Voraz (Primero el Mejor) con la heurística definida.
camino, costo_total = busqueda_voraz_primero_el_mejor(grafo, inicio, objetivo, heuristica_distancia)

# Imprimimos el camino encontrado y el costo total.
print("Camino encontrado:", camino)
print("Costo total:", costo_total)
