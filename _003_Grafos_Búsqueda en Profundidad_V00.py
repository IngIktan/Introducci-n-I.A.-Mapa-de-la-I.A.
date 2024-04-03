# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en profundidad en un grafo dado.

# Definición de la función para la búsqueda en profundidad
def busqueda_en_profundidad(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()  # Conjunto para almacenar nodos visitados
    # Marcar el nodo actual como visitado
    visitados.add(inicio)
    print("Visitando nodo:", inicio)
    # Recorrer los nodos adyacentes al nodo actual
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            # Llamar recursivamente a la función para los nodos adyacentes no visitados
            busqueda_en_profundidad(grafo, vecino, visitados)

# Grafo de ejemplo representado como un diccionario de conjuntos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Llamar a la función de búsqueda en profundidad con el grafo y el nodo inicial 'A'
busqueda_en_profundidad(grafo, 'A')

