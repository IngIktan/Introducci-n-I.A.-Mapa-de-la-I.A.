# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en profundidad iterativa en un grafo dado.

# Definición de la función para la búsqueda en profundidad iterativa
def busqueda_en_profundidad_iterativa(grafo, inicio, max_profundidad):
    for profundidad in range(max_profundidad):
        # Llamar a la función de búsqueda en profundidad limitada con la profundidad actual
        busqueda_en_profundidad_limitada(grafo, inicio, profundidad)

# Función para la búsqueda en profundidad limitada
def busqueda_en_profundidad_limitada(grafo, inicio, limite, visitados=None)
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

# Definir la máxima profundidad para la búsqueda iterativa
max_profundidad = 3

# Llamar a la función de búsqueda en profundidad iterativa con el grafo, el nodo inicial 'A' y la máxima profundidad
busqueda_en_profundidad_iterativa(grafo, 'A', max_profundidad)
