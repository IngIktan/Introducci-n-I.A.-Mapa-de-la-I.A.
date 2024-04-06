# Daniel Alejandro Flores Sepulveda
# Ejemplo básico de Búsqueda en Línea

import random

# Función para generar el mapa aleatorio
def generar_mapa(filas, columnas, probabilidad_obstaculo):
    mapa = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            if random.random() < probabilidad_obstaculo:
                fila.append(1)  # Obstáculo
            else:
                fila.append(0)  # Espacio libre
        mapa.append(fila)
    return mapa

# Función para imprimir el mapa
def imprimir_mapa(mapa):
    for fila in mapa:
        print("".join(["#" if c == 1 else " " for c in fila]))

# Función para encontrar la siguiente posición válida en la dirección especificada
def siguiente_posicion_valida(mapa, fila_actual, columna_actual, direccion):
    filas, columnas = len(mapa), len(mapa[0])
    # Definir los desplazamientos para cada dirección (arriba, abajo, izquierda, derecha)
    desplazamientos = {"arriba": (-1, 0), "abajo": (1, 0), "izquierda": (0, -1), "derecha": (0, 1)}
    fila_nueva, columna_nueva = fila_actual + desplazamientos[direccion][0], columna_actual + desplazamientos[direccion][1]
    # Verificar si la nueva posición está dentro del mapa y no es un obstáculo
    if 0 <= fila_nueva < filas and 0 <= columna_nueva < columnas and mapa[fila_nueva][columna_nueva] == 0:
        return fila_nueva, columna_nueva
    return fila_actual, columna_actual

# Función para realizar la búsqueda en línea
def busqueda_en_linea(mapa, fila_inicial, columna_inicial, direccion_inicial, pasos_maximos):
    fila_actual, columna_actual = fila_inicial, columna_inicial
    direccion_actual = direccion_inicial
    pasos_restantes = pasos_maximos
    while pasos_restantes > 0:
        fila_actual, columna_actual = siguiente_posicion_valida(mapa, fila_actual, columna_actual, direccion_actual)
        imprimir_mapa(mapa)  # Imprimir el mapa en cada paso (solo para demostración)
        print("Posición actual:", fila_actual, columna_actual)  # Mostrar la posición actual
        # Simular algún tipo de lógica para actualizar la dirección actual (puede ser aleatoria)
        direccion_actual = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        pasos_restantes -= 1

# Parámetros del problema
filas, columnas = 10, 10  # Tamaño del mapa
probabilidad_obstaculo = 0.2  # Probabilidad de que una celda sea un obstáculo
fila_inicial, columna_inicial = 0, 0  # Posición inicial del personaje
direccion_inicial = "derecha"  # Dirección inicial del movimiento
pasos_maximos = 20  # Número máximo de pasos a tomar

# Generar el mapa
mapa = generar_mapa(filas, columnas, probabilidad_obstaculo)

# Realizar la búsqueda en línea
busqueda_en_linea(mapa, fila_inicial, columna_inicial, direccion_inicial, pasos_maximos)
