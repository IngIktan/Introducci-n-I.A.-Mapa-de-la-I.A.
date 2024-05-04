# Autor: Daniel Alejandro Flores Sepulveda
# Descripción: Implementación básica del algoritmo GRAPHPLAN en Python utilizando la biblioteca networkx

import networkx as nx

def graphplan(estado_inicial, objetivos):
    # Crear un grafo dirigido
    grafo = nx.DiGraph()

    # Agregar nodos de nivel 0 (acciones disponibles en el estado inicial)
    for accion in estado_inicial:
        grafo.add_node(accion, level=0)

    # Agregar nodos de nivel 1 (acciones que llevan al estado objetivo)
    for objetivo in objetivos:
        grafo.add_node(objetivo, level=1)

    # Agregar arcos (relaciones de precondición y efecto entre acciones)
    for accion in estado_inicial:
        for objetivo in objetivos:
            if accion.precondiciones == objetivo.efectos:
                grafo.add_edge(accion, objetivo)

    # Calcular niveles adicionales
    niveles = 1
    while True:
        nivel_actual = [accion for accion, datos in grafo.nodes(data=True) if datos["level"] == niveles]
        acciones_nivel_anterior = [accion for accion, datos in grafo.nodes(data=True) if datos["level"] == niveles - 1]

        for accion_actual in nivel_actual:
            for accion_anterior in acciones_nivel_anterior:
                if all(efecto in accion_anterior.efectos for efecto in accion_actual.precondiciones):
                    grafo.add_node(accion_actual, level=niveles+1)
                    grafo.add_edge(accion_anterior, accion_actual)

        if all(grafo.nodes[accion]["level"] > 0 for accion in objetivos):
            break

        niveles += 1

    return grafo

# Definir clase para acciones
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

# Definir estado inicial y objetivos
estado_inicial = [Accion("accion1", [], ["a"]), Accion("accion2", [], ["b"])]
objetivos = [Accion("accion3", ["a"], ["c"]), Accion("accion4", ["b"], ["d"])]

# Ejecutar el algoritmo GRAPHPLAN
grafo_plan = graphplan(estado_inicial, objetivos)

# Imprimir el grafo resultante
print("Grafo de planificación:")
print(grafo_plan.nodes)
print(grafo_plan.edges)
