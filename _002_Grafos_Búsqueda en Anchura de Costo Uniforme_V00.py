# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en anchura de costo uniforme en un grafo dado.

import heapq

# Definición de la función para la búsqueda en anchura de costo uniforme
def busqueda_en_anchura_costo_uniforme(grafo, inicio):
    visitados = set()  # Conjunto para almacenar nodos visitados
    cola_prioridad = [(0, inicio)]  # Cola de prioridad para seguir los nodos a visitar
    
    # Mientras la cola de prioridad no esté vacía
    while cola_prioridad:
        # Obtener el nodo con menor costo de la cola de prioridad
        costo, nodo_actual = heapq.heappop(cola_prioridad)
        # Si el nodo actual no ha sido visitado
        if nodo_actual not in visitados:
            # Marcar el nodo actual como visitado
            visitados.add(nodo_actual)
            print("Visitando nodo:", nodo_actual, "con costo:", costo)
            # Recorrer los nodos adyacentes al nodo actual
            for vecino, costo_vecino in grafo[nodo_actual].items():
                # Si el vecino no ha sido visitado
                if vecino not in visitados:
                    # Calcular el costo acumulado hasta el vecino
                    costo_acumulado = costo + costo_vecino
                    # Agregar el vecino a la cola de prioridad con su costo acumulado
                    heapq.heappush(cola_prioridad, (costo_acumulado, vecino))

# Grafo de ejemplo representado como un diccionario de diccionarios con los costos de las aristas
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 3},
    'C': {'A': 2, 'F': 4},
    'D': {'B': 5},
    'E': {'B': 3, 'F': 1},
    'F': {'C': 4, 'E': 1}
}

# Llamar a la función de búsqueda en anchura de costo uniforme con el grafo y el nodo inicial 'A'
busqueda_en_anchura_costo_uniforme(grafo, 'A')
