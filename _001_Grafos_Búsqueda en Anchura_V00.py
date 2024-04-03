# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en anchura en un grafo dado.

from collections import deque

# Definición de la función para la búsqueda en anchura
def busqueda_en_anchura(grafo, inicio):
    visitados = set()  # Conjunto para almacenar nodos visitados
    cola = deque([inicio])  # Cola para seguir los nodos a visitar
    
    # Mientras la cola no esté vacía
    while cola:
        # Sacar el primer nodo de la cola
        nodo_actual = cola.popleft()
        # Si el nodo actual no ha sido visitado
        if nodo_actual not in visitados:
            # Marcar el nodo actual como visitado
            visitados.add(nodo_actual)
            print("Visitando nodo:", nodo_actual)
            # Agregar los nodos adyacentes no visitados a la cola
            cola.extend(grafo[nodo_actual] - visitados)

# Grafo de ejemplo representado como un diccionario de conjuntos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Llamar a la función de búsqueda en anchura con el grafo y el nodo inicial 'A'
busqueda_en_anchura(grafo, 'A')
