# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de planificación de orden parcial en Python utilizando la biblioteca networkx

import networkx as nx

# Crear un grafo dirigido
grafo = nx.DiGraph()

# Agregar nodos (acciones)
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("D")

# Agregar arcos (relaciones de precedencia entre acciones)
grafo.add_edge("A", "B")
grafo.add_edge("A", "C")
grafo.add_edge("B", "D")
grafo.add_edge("C", "D")

# Calcular el orden parcial
orden_parcial = nx.topological_sort(grafo)

# Imprimir el orden parcial
print("Orden parcial de las acciones:")
for accion in orden_parcial:
    print(accion)
