# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Ejemplo de representación de una taxonomía de categorías y objetos utilizando networkx

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para representar la taxonomía
G = nx.DiGraph()

# Agregar nodos (categorías y objetos)
G.add_node("Animal")
G.add_node("Mamífero")
G.add_node("Perro")
G.add_node("Gato")

# Agregar relaciones de subcategoría (aristas dirigidas)
G.add_edge("Animal", "Mamífero")
G.add_edge("Mamífero", "Perro")
G.add_edge("Mamífero", "Gato")

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()
