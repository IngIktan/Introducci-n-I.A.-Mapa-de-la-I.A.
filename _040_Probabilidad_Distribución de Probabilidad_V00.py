# Daniel Alejandro Flores Sepulveda
# Programa para calcular la distribución de probabilidad de un conjunto de eventos

# Definición de la función para calcular la distribución de probabilidad
def distribucion_probabilidad(eventos, espacio_muestral):
    distribucion = {}
    total_eventos = len(espacio_muestral)
    for evento in eventos:
        ocurrencias_evento = espacio_muestral.count(evento)
        distribucion[evento] = ocurrencias_evento / total_eventos
    return distribucion

# Definición del espacio muestral
espacio_muestral = ['cara', 'cara', 'cruz', 'cara', 'cruz', 'cara', 'cruz']

# Eventos para calcular la distribución de probabilidad
eventos = ['cara', 'cruz']

# Cálculo de la distribución de probabilidad
distribucion = distribucion_probabilidad(eventos, espacio_muestral)

# Impresión del resultado
print("Distribución de probabilidad:")
for evento, probabilidad in distribucion.items():
    print(f"{evento}: {probabilidad}")
