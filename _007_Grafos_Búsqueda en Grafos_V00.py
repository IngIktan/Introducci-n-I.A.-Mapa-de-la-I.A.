
# Daniel Alejandro Flores Sepulveda
# Programa para realizar una búsqueda en grafos (cualquier tipo de búsqueda) en un grafo dado.

# Definición de la función para la búsqueda en grafos
def busqueda_en_grafos(grafo, inicio, objetivo, metodo):
    # Método para llamar a la función de búsqueda adecuada
    if metodo == "anchura":
        return busqueda_en_anchura(grafo, inicio, objetivo)
    elif metodo == "profundidad":
        return busqueda_en_profundidad(grafo, inicio, objetivo)
    elif metodo == "bidireccional":
        return busqueda_bidireccional(grafo, inicio, objetivo)
    else:
        print("Método de búsqueda no válido.")
        return None

# Función para la búsqueda en anchura
def busqueda_en_anchura(grafo, inicio, objetivo):
    # Implementación de la búsqueda en anchura
    visitados = set()  # Conjunto para almacenar nodos visitados
    cola = [inicio]  # Cola para seguir los nodos a visitar
    
    # Mientras la cola no esté vacía
    while cola:
        # Obtener el nodo actual de la cola
        nodo_actual = cola.pop(0)
        # Si el nodo actual es el objetivo, retornarlo
        if nodo_actual == objetivo:
            return nodo_actual
        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)
        # Agregar los nodos adyacentes no visitados a la cola
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                cola.append(vecino)
    # Si no se encuentra el objetivo, retornar None
    return None

# Función para la búsqueda en profundidad
def busqueda_en_profundidad(grafo, inicio, objetivo):
    # Implementación de la búsqueda en profundidad
    def dfs(grafo, nodo_actual, objetivo, visitados):
        # Si el nodo actual es el objetivo, retornarlo
        if nodo_actual == objetivo:
            return nodo_actual
        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)
        # Recorrer los nodos adyacentes al nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                resultado = dfs(grafo, vecino, objetivo, visitados)
                if resultado:
                    return resultado
        return None
    
    # Conjunto para almacenar nodos visitados
    visitados = set()
    # Llamar a la función de búsqueda en profundidad
    return dfs(grafo, inicio, objetivo, visitados)

# Función para la búsqueda bidireccional
def busqueda_bidireccional(grafo, inicio, objetivo):
    # Implementación de la búsqueda bidireccional
    visitados_inicio = set()  # Conjunto para almacenar nodos visitados desde el inicio
    visitados_objetivo = set()  # Conjunto para almacenar nodos visitados desde el objetivo
    cola_inicio = [inicio]  # Cola para seguir los nodos a visitar desde el inicio
    cola_objetivo = [objetivo]  # Cola para seguir los nodos a visitar desde el objetivo
    
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

# Método de búsqueda a utilizar ("anchura", "profundidad" o "bidireccional")
metodo_busqueda = "anchura"

# Realizar la búsqueda en grafos con el método especificado
resultado = busqueda_en_grafos(grafo, inicio, objetivo, metodo_busqueda)
if resultado is not None:
    print("Resultado de la búsqueda:", resultado)
else:
    print("No se encontró un camino entre", inicio, "y", objetivo)
