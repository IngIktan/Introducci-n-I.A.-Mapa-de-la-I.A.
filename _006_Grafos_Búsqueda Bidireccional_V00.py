# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda bidireccional en un grafo dado.

# Definición de la función para la búsqueda bidireccional
def busqueda_bidireccional(grafo, inicio, objetivo):
    # Conjuntos para almacenar nodos visitados desde el inicio y desde e objetivo
    visitados_inicio = set()
    visitados_objetivo = set()
    # Colas para seguir los nodos a visitar desde el inicio y desde el objetivo
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]
    
    # Mientras ambas colas no estén vacías
    while cola_inicio and cola_objetivo:
        # Buscar en la dirección desde el inicio
        nodo_actual_inicio = cola_inicio.pop(0)
        if nodo_actual_inicio in visitados_objetivo:
            return nodo_actual_inicio  # Si el nodo actual es visitado desde el objetivo, se encontró el camino
        visitados_inicio.add(nodo_actual_inicio)
        for vecino in grafo[nodo_actual_inicio]:
            if vecino not in visitados_inicio:
                cola_inicio.append(vecino)
        
        # Buscar en la dirección desde el objetivo
        nodo_actual_objetivo = cola_objetivo.pop(0)
        if nodo_actual_objetivo in visitados_inicio:
            return nodo_actual_objetivo  # Si el nodo actual es visitado desde el inicio, se encontró el camino
        visitados_objetivo.add(nodo_actual_objetivo)
        for vecino in grafo[nodo_actual_objetivo]:
            if vecino not in visitados_objetivo:
                cola_objetivo.append(vecino)
    
    return None  # Si no se encuentra el camino

# Grafo de ejemplo representado como un diccionario de conjuntos
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Definir el nodo inicial y el nodo objetivo para la búsqueda
inicio = 'A'
objetivo = 'F'

# Realizar la búsqueda bidireccional y obtener el resultado
resultado = busqueda_bidireccional(grafo, inicio, objetivo)
if resultado is not None:
    print("Se encontró el camino entre", inicio, "y", objetivo, ":")
    print(resultado)
else:
    print("No se encontró un camino entre", inicio, "y", objetivo)
