# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en profundidad limitada en un grafo dado.

# Definición de la función para la búsqueda en profundidad limitada
def busqueda_en_profundidad_limitada(grafo, inicio, limite, visitados=None):
    if visitados is None:
        visitados = set()  # Conjunto para almacenar nodos visitados
    # Marcar el nodo actual como visitado
    visitados.add(inicio)
    print("Visitando nodo:", inicio)
    # Si se alcanza el límite de profundidad, detener la búsqueda
    if limite == 0:
        return
    # Recorrer los nodos adyacentes al nodo actual
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            # Llamar recursivamente a la función para los nodos adyacentes con límite reducido
            busqueda_en_profundidad_limitada(grafo, vecino, limite - 1, visitados)

# Grafo de ejemplo representado como un diccionario de conjuntos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Definir el límite de profundidad para la búsqueda
limite_profundidad = 2

# Llamar a la función de búsqueda en profundidad limitada con el grafo, el nodo inicial 'A' y el límite de profundidad
busqueda_en_profundidad_limitada(grafo, 'A', limite_profundidad)
